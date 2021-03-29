"""
    asenkron olarak log kaydının kafkaya iletilmesi
"""


import time
from kafka import KafkaProducer
from kafka.errors import KafkaError
import asyncio

producer = KafkaProducer(bootstrap_servers=["192.168.1.112:9092"],client_id="my_p_id")

last_index=0


async def lastSent():
    fileHandle = open ( 'log.log',"r" )
    lineList = fileHandle.readlines()
    fileHandle.close()
    return lineList[-1]

async def send(veri):
    # future = producer.send('logs2',b"py den mesaj",partition=1)
    future = producer.send('logs2',veri.encode())
    try:record_metadata = future.get(timeout=10)
    except KafkaError:log.exception()

async def main():
    last=""
    while 1:
        now=await lastSent()
        if now!=last:
            await send(now)
        last=now

        time.sleep(0.05)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
