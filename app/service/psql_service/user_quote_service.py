from typing import Dict
from returns.maybe import Nothing, Some, Maybe
from toolz import pipe
from toolz.curried import partial

from app.db.models import UserQuote
from app.repository.psql.user_quote_repository import insert_user_quote
from app.utils.model_utils import has_all_keys


def create_user_quote(user_quote_dict: Dict[str, str], location_id: int, device_info_id: int) -> UserQuote:
    return UserQuote(
        username=user_quote_dict["username"],
        email=user_quote_dict["email"],
        ip_address=user_quote_dict["ip_address"],
        created_at=user_quote_dict["created_at"],
        location_id=location_id,
        device_info_id=device_info_id
    )

def extract_user_quote(message) -> Dict[str, str]:
    return {
        "username": message["username"],
        "email": message["email"],
        "ip_address": message["ip_address"],
        "created_at": message["created_at"]
    }


def convert_to_user_quote(user_quote_json: Dict[str, str],location_id: int, device_info_id: int) -> Maybe[UserQuote]:
    return pipe(
        user_quote_json,
        has_all_keys(['username', 'email', 'ip_address', 'created_at']),
        lambda is_valid: Nothing if not is_valid else Some(create_user_quote(user_quote_json, location_id, device_info_id))
    )

def create_user_quote_service(message: Dict[str, str], location_id: int, device_info_id: int):
    return pipe(
        message,
        extract_user_quote,
        lambda user_quote_json: convert_to_user_quote(user_quote_json, location_id, device_info_id),
        lambda user: insert_user_quote(user.value_or(None)) if user.value_or(None) else None
    )