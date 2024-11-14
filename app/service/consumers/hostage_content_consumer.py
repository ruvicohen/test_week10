import os

from dotenv import load_dotenv

from app.kafka_settings.consume import consume

load_dotenv(verbose=True)


hostage_content_topic = os.environ['TOPIC_MESSAGE_HOSTAGE']

def consume_hostage_content(topic):
    consume(topic, None)

if __name__ == '__main__':
    consume_hostage_content(hostage_content_topic)
