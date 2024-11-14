import os

from dotenv import load_dotenv

from app.kafka_settings.consume import consume
from app.repository.mongodb.user_quote_repository import insert_email

load_dotenv(verbose=True)

email_topic = os.environ['TOPIC_MESSAGE_ALL']

def consume_feedback(topic):
    consume(topic, insert_email)

if __name__ == '__main__':
    consume_feedback(email_topic)