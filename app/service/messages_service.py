import re
from typing import Dict, Any, List

from toolz import pipe


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
    pass

def handle_insert_message_explos(message):
    pass