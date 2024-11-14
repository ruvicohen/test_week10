import re
from collections import Counter
from itertools import chain

from toolz import pipe
from toolz.curried import partial, reduce

from app.repository.psql.explosive_content_repository import get_explosive_content
from app.repository.psql.hostage_content_repository import get_hostage_content
from app.service.psql_service.device_info_service import create_device_info_service
from app.service.psql_service.explose_content_service import create_explos_content_service
from app.service.psql_service.hostage_content_service import create_hostage_content_service
from app.service.psql_service.location_service import create_location_service
from app.service.psql_service.user_quote_service import create_user_quote_service, extract_user_quote


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
    explosive_sentences = get_explosive_content()
    hostage_sentences = get_hostage_content()

    words = list(
        chain(*map(lambda sentence: sentence[0].split(), explosive_sentences + hostage_sentences))
    )

    word_counts = Counter(words)

    most_common_word, frequency = word_counts.most_common(1)[0]

    return most_common_word, frequency

def get_most_common_word1():
    # הפעלת pipe על התוצאות של הפונקציות
    return pipe(
        (get_explosive_content(), get_hostage_content()),  # הפונקציות שמחזירות את התוכן
        lambda content: reduce(lambda x, y: x + y, map(lambda sentence: sentence[0].split(), content)),
        Counter,
        lambda counter: counter.most_common(1)[0][0]
    )


print(get_most_common_word1())
def get_most_common_word3():
    # שליפת התוכן מהטבלאות
    explosive_sentences = get_explosive_content()  # שליפת התוכן מהטבלה המתאימה
    hostage_sentences = get_hostage_content()  # שליפת התוכן מהטבלה המתאימה

    # שימוש ב-map לפיצול כל משפט למילים ו-extend כל המילים לרשימה אחת
    # Flatten the list (since map returns a list of lists)
    words = reduce(lambda x, y: x + y,
                   map(lambda sentence: sentence[0].split(), explosive_sentences + hostage_sentences))

    # ספירת המילים עם Counter
    word_counts = Counter(words)

    # מציאת המילה הכי נפוצה
    most_common_word, frequency = word_counts.most_common(1)[0]

    return most_common_word, frequency


# קריאה לפונקציה
word, count = get_most_common_word3()
print(f"The most common word is '{word}' and it appears {count} times.")

# קריאה לפונקציה
word, count = get_most_common_word()
print(f"The most common word is '{word}' and it appears {count} times.")
