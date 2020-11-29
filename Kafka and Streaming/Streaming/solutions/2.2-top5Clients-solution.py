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

orders = filestream.flatMap(parseOrder)

from operator import add

# Calculate total number of buy/sell orders (buy -> key = True, sell -> key = False)
numPerType = orders.map(lambda o: ("BUY", 1) if o['buy'] else ("SELL", 1)).reduceByKey(add)

volumePerClient = orders.map(lambda o: (o['clientId'], o['amount'] * o['price']))
volumeState = volumePerClient.updateStateByKey(lambda vals, totalOpt: sum(vals) + totalOpt if totalOpt != None else sum(vals))

top5clients = volumeState.transform(lambda rdd: rdd.sortBy(lambda x: x[1], False).map(lambda x: x[0]).zipWithIndex().filter(lambda x: x[1] < 5))

top5clList = top5clients.repartition(1).map(lambda x: str(x[0])).glom().map(lambda arr: ("TOP5CLIENTS", arr))

finalStream = numPerType.union(top5clList)
finalStream.pprint()

#finalStream.repartition(1).saveAsTextFiles(STREAM_OUT, "txt")

# updateStateByKey requires checkpointing; set the spark checkpoint
# folder to the subfolder of the current folder named "checkpoint"
sc.setCheckpointDir("checkpoint")

ssc.start()
ssc.awaitTermination()


