from typing import List, Dict

from toolz import curry


@curry
def has_all_keys(keys: List[str], d: Dict[str, str]) -> bool:
    return all(k in d for k in keys)
