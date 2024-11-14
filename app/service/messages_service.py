import re
from collections import Counter
from itertools import chain
from toolz import pipe
from toolz.curried import partial, reduce
from app.repository.psql_repository.explosive_content_repository import get_explosive_content
from app.repository.psql_repository.hostage_content_repository import get_hostage_content
from app.service.psql_service.device_info_service import create_device_info_service
from app.service.psql_service.explose_content_service import create_explos_content_service
from app.service.psql_service.hostage_content_service import create_hostage_content_service
from app.service.psql_service.location_service import create_location_service
from app.service.psql_service.user_quote_service import create_user_quote_service

def check_sentence_with_partial_word(sentences, partial_word):
    return pipe(
        fr'\b{re.escape(partial_word)}\w*',
        lambda pattern: any(map(lambda sentence:
                                bool(re.search(pattern, sentence, re.IGNORECASE)), sentences))
        )

def reorder_sentences_by_danger(obj: dict, partial_word: str) -> dict:
    def is_dangerous(sentence: str) -> bool:
        return check_sentence_with_partial_word([sentence], partial_word)

    obj['sentences'] = sorted(obj['sentences'], key=is_dangerous, reverse=True)
    return obj

def handle_insert_message_hostage(message):
    device_id = create_device_info_service(message['device_info']).value_or(None).device_info_id
    location_id = create_location_service(message['location']).value_or(None).location_id
    user_quote_id = create_user_quote_service(message, location_id, device_id).value_or(None).user_quote_id
    create_hostage_content_service(message['sentences'], user_quote_id)

def handle_insert_message_explos(message):
    device_id = create_device_info_service(message['device_info']).value_or(None).device_info_id
    location_id = create_location_service(message['location']).value_or(None).location_id
    user_quote_id = create_user_quote_service(message, location_id, device_id).value_or(None).user_quote_id
    create_explos_content_service(message['sentences'], user_quote_id)

def get_most_common_word():
    try:
        return pipe(
            (get_explosive_content() + get_hostage_content()),
            partial(map, lambda sentence: sentence[0].split()),
            partial(chain.from_iterable),
            Counter,
            list,
            lambda words: words[0]
        )
    except Exception:
        return None