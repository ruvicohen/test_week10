from app.db.models import SuspiciousHostageContent
from app.repository.psql.hostage_content_repository import insert_hostage_content

def create_suspicious_hostage_content(sentence, user_quote_id) -> SuspiciousHostageContent:
    return SuspiciousHostageContent(
        sentence=sentence,
        user_quote_id=user_quote_id
    )


def create_hostage_content_service(messages_json, user_quote_id):
    for message in messages_json:
        hostage_content = create_suspicious_hostage_content(message, user_quote_id)
        insert_hostage_content(hostage_content)