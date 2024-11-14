import json
import os
from dotenv import load_dotenv
from kafka import KafkaConsumer

load_dotenv(verbose=True)

def consume(topic, function):
    consumer = KafkaConsumer(
        topic,
        bootstrap_servers=os.environ['BOOTSTRAP_SERVERS'],
        value_deserializer=lambda m: json.loads(m.decode('utf-8'))
    )

    for message in consumer:
        function(message.value)
        print(f'Received: {message.key}: {message.value}')