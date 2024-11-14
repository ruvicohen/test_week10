from typing import Dict
from returns.maybe import Nothing, Some, Maybe
from toolz import pipe
from app.db.models import SuspiciousHostageContent
from app.repository.psql.hostage_content_repository import insert_hostage_content
from app.service.consumers.hostage_content_consumer import consume_hostage_content
from app.utils.model_utils import has_all_keys

def create_suspicious_hostage_content(content_dict: Dict[str, str], user_quote_id) -> SuspiciousHostageContent:
    return SuspiciousHostageContent(
        sentence=content_dict["sentence"],
        user_quote_id=user_quote_id
    )


def convert_to_suspicious_hostage_content(content_json: Dict[str, str], user_quote_id) -> Maybe[SuspiciousHostageContent]:
    return pipe(
        content_json,
        has_all_keys(['sentence', 'user_quote_id']),
        lambda is_valid: Nothing if not is_valid else Some(create_suspicious_hostage_content(content_json, user_quote_id))
    )

def create_hostage_content_service(messages_json, user_quote_id):
    for message in messages_json:
        hostage_content = convert_to_suspicious_hostage_content(message, user_quote_id)
        insert_hostage_content(hostage_content)