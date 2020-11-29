#!/usr/bin/env python
import os
import time
import pwd

from kafka import KafkaProducer
from kafka.errors import KafkaError


STREAM_IN = 'stream-IN'
SLEEP = 0.5 #seconds

# Get the full path to this script
scriptPath = os.path.dirname(os.path.realpath(__file__))

# calculate the path of the orders file
ordersFile = scriptPath + "/../data/orders.txt"

# Calculate the topic name
topic = pwd.getpwuid( os.getuid() )[ 0 ] + ".orders"

print("Reading data from %s" % ordersFile)
print("Sending orders data to Kafka topic %s" % topic)

try:
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

    with open(ordersFile) as f:
        for line in f:
            producer.send(topic, str(line).encode())
            time.sleep(SLEEP)

    print("\n DONE - All data sent !")
except KeyboardInterrupt:
    print("Terminating ...")

finally:
    producer.close()
        
    
