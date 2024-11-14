import os
from app.kafka_settings.consume import consume
from app.repository.email_repository import insert_email

email_topic = os.environ['TOPIC_MESSAGE_ALL']

def consume_feedback(topic):
    consume(topic, insert_email)

if __name__ == '__main__':
    consume_feedback(email_topic)