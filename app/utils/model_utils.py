from typing import List, Dict
from dictalchemy import asdict
from toolz import curry


@curry
def has_all_keys(keys: List[str], d: Dict[str, str]) -> bool:
    return all(k in d for k in keys)

def convert_user_quote_to_json(user_data):
    return {   'email info': asdict(user_data),
                'device': asdict(user_data.device),
                'location': asdict(user_data.location),
                'sentences': ([sentence.sentence for sentence in user_data.explosive_sentences] +
                            [sentence.sentence for sentence in user_data.hostage_sentences])
                }