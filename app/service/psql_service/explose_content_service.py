from typing import Dict
from returns.maybe import Nothing, Some, Maybe
from toolz import pipe

from app.repository.psql.explosive_content_repository import insert_explosive_content
from app.utils.model_utils import has_all_keys
from app.db.models import SuspiciousExplosiveContent


def create_suspicious_explosive_content(content_dict: Dict[str, str], user_quote_id) -> SuspiciousExplosiveContent:
    return SuspiciousExplosiveContent(
        sentence=content_dict["sentence"],
        user_quote_id=user_quote_id
    )


def convert_to_suspicious_explosive_content(content_json: Dict[str, str], user_quote_id) -> Maybe[SuspiciousExplosiveContent]:
    return pipe(
        content_json,
        has_all_keys(['sentence', 'user_quote_id']),
        lambda is_valid: Nothing if not is_valid else Some(create_suspicious_explosive_content(content_json, user_quote_id))
    )

def create_explos_content_service(messages_json, user_quote_id):
    for message in messages_json:
        explose_content = convert_to_suspicious_explosive_content(message, user_quote_id)
        insert_explosive_content(explose_content)