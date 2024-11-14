from toolz import pipe

from app.db.models import SuspiciousExplosiveContent


def create_suspicious_explosive_content(content_dict: Dict[str, str]) -> SuspiciousExplosiveContent:
    return SuspiciousExplosiveContent(
        sentence=content_dict["sentence"],
        user_quote_id=content_dict["user_quote_id"]
    )


def convert_to_suspicious_explosive_content(content_json: Dict[str, str]) -> Maybe[SuspiciousExplosiveContent]:
    return pipe(
        content_json,
        has_all_keys(['sentence', 'user_quote_id']),
        lambda is_valid: Nothing if not is_valid else Some(create_suspicious_explosive_content(content_json))
    )