import os
from dotenv import load_dotenv
from app.kafka_settings.consume import consume

load_dotenv(verbose=True)

explosive_content_topic = os.environ['TOPIC_MESSAGE_EXPLOSIVE']

def consume_explosive_content(topic):
    from app.service.messages_service import handle_insert_message_explos
    consume(topic, handle_insert_message_explos)

if __name__ == '__main__':
    consume_explosive_content(explosive_content_topic)