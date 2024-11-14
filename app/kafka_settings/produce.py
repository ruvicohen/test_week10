import json
import os
from dotenv import load_dotenv
from kafka import KafkaProducer

load_dotenv(verbose=True)

def produce(topic, key, value):
    producer = KafkaProducer(
        bootstrap_servers=os.environ['BOOTSTRAP_SERVERS'],
        value_serializer=lambda v: json.dumps(v).encode('utf-8'),
    )
    producer.send(topic, value=value, key=key.encode('utf-8'))