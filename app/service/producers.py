import os
from dotenv import load_dotenv
from app.kafka_settings.produce import produce
from app.service.messages_service import check_sentence_with_partial_word, reorder_sentences_by_danger

load_dotenv(verbose=True)

user_quote_topic = os.environ['TOPIC_MESSAGE_ALL']
hostage_content_topic = os.environ['TOPIC_MESSAGE_HOSTAGE']
explosive_content_topic = os.environ['TOPIC_MESSAGE_EXPLOSIVE']

def produce_user_quote(message):
    produce(user_quote_topic, message['email'], message)

def produce_hostage_content(message):
    produce(hostage_content_topic, message['email'], message)

def produce_explosive_content(message):
    produce(explosive_content_topic, message['email'], message)

def handle_producers(message):
    produce_user_quote(message)
    if check_sentence_with_partial_word(message['sentences'], 'hostage'):
        message = reorder_sentences_by_danger(message, 'hostage')
        produce_hostage_content(message)

    if check_sentence_with_partial_word(message['sentences'], 'explos'):
        message = reorder_sentences_by_danger(message, 'explos')
        produce_explosive_content(message)
