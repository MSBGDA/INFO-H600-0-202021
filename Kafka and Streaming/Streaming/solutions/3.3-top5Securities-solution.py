import sys
import os
from datetime import datetime
from pathlib import Path

STREAM_IN = 'stream-IN'
STREAM_OUT = 'stream-OUT'

# We first delete all files from the STREAM_IN folder
# before starting spark streaming.
# This way, all files are new
print("Deleting existing files in %s ..." % STREAM_IN)
p = Path('.') / STREAM_IN
for f in p.glob("*.ordtmp"):
  os.remove(f)
print("... done")

from pyspark import SparkContext, SparkConf
from pyspark.streaming import StreamingContext

sc = SparkContext("local[*]", "CountAndVolumePerBatch")
sc.setLogLevel("WARN")   #Make sure warnings and errors observed by spark are printed.

ssc = StreamingContext(sc, 5)  #generate a mini-batch every 5 seconds
filestream = ssc.textFileStream(STREAM_IN) #monitor new files in folder stream-IN

def parseOrder(line):
  '''parses a single line in the orders file'''
  s = line.split(",")
  try:
      if s[6] != "B" and s[6] != "S":
        raise Exception('Wrong format')
      return [{"time": datetime.strptime(s[0], "%Y-%m-%d %H:%M:%S"),
               "orderId": int(s[1]), 
               "clientId": int(s[2]),
               "symbol": s[3], 
               "amount": int(s[4]), 
               "price":  float(s[5]), 
               "buy": s[6] == "B"}]
  except Exception as err:
      print("Wrong line format (%s): %s" % (line,err))
      return []

from operator import add, sub
orders = filestream.flatMap(parseOrder)
stocksPerWindow = orders.map(lambda x: (x['symbol'], x['amount'])).reduceByKeyAndWindow(add, sub, 180, 15)

topStocks = stocksPerWindow.transform(lambda rdd: rdd.sortBy(lambda x: x[1], False).map(lambda x: x[0]).\
zipWithIndex().filter(lambda x: x[1] < 5)).repartition(1).\
map(lambda x: str(x[0])).glom().\
map(lambda arr: ("TOP5STOCKS", arr))

topStocks.pprint()

# windows operations requires checkpointing; set the spark checkpoint
# folder to the subfolder of the current folder named "checkpoint"
sc.setCheckpointDir("checkpoint")

ssc.start()
ssc.awaitTermination()


