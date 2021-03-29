from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from kafka import KafkaProducer
from kafka.errors import KafkaError
import json
import time

@csrf_exempt
def hello(request):
    request.start_time = time.time()

    
    # producer = KafkaProducer(
    # bootstrap_servers=["192.168.1.112:9092"],
    # client_id="my_p_id"
    # )

    total = (time.time() - request.start_time)*1000
    sent=request.method+","+str(total)+","+str(time.time())

    # future = producer.send('logs2',sent.encode(),)
    # try:record_metadata = future.get(timeout=10)
    # except KafkaError:log.exception()

    
    with open(str("log.txt"), "a") as dosya:
        dosya.write(sent+"\n")

    return HttpResponse("hello world")
