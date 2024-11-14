from app.repository.psql_repository.explosive_content_repository import insert_explosive_content
from app.db.models import SuspiciousExplosiveContent

def create_suspicious_explosive_content(sentence, user_quote_id) -> SuspiciousExplosiveContent:
    return SuspiciousExplosiveContent(
        sentence=sentence,
        user_quote_id=user_quote_id
    )

def create_explos_content_service(messages_json, user_quote_id):
    for message in messages_json:
        explos_content = create_suspicious_explosive_content(message, user_quote_id)
        insert_explosive_content(explos_content)