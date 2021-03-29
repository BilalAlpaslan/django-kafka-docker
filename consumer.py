"""
    kafkadaki verilerin mongodb ye kaydı
"""

from kafka import KafkaConsumer
import pymongo
import json


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["myDatabase"]
mycol = mydb["logs"]




consumer = KafkaConsumer(
    'logs2',
    group_id='my-group',
    client_id="my_py_id",
    bootstrap_servers=["192.168.1.112:9092"])

for message in consumer:
    # e.g., for unicode: `message.value.decode('utf-8')`
    # print("%s:%d:%d: key=%s value=%s" % (
    #     message.topic, message.partition,message.offset, message.key,message.value
    #     ))
    mydict = { "log": message.value.decode() }
    x = mycol.insert_one(mydict)