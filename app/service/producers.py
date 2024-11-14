import os
from app.kafka_settings.produce import produce

email_topic = os.environ['TOPIC_MESSAGE_ALL']

def produce_new_email(email):
    produce(email_topic, email['email'], email)