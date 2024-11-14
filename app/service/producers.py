import os
from app.kafka_settings.produce import produce

user_quote_topic = os.environ['TOPIC_MESSAGE_ALL']

def produce_user_quote(message):
    produce(user_quote_topic, message['email'], message)