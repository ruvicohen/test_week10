from collections import Counter

from returns.result import Result, Failure, Success

from app.db.models import SuspiciousExplosiveContent, SuspiciousHostageContent
from app.db.psql_db import session_maker
from app.repository.psql.hostage_content_repository import get_hostage_content
from app.repository.psql.user_quote_repository import get_user_quote_by_id


def insert_explosive_content(explosive_content: SuspiciousExplosiveContent) \
        -> Result[SuspiciousExplosiveContent, str]:
    with session_maker() as session:
        try:
            user_quote_id = explosive_content.user_quote_id
            if get_user_quote_by_id(user_quote_id).value_or(None) is None:
                return Failure("user quote not found")
            session.add(explosive_content)
            session.commit()
            session.refresh(explosive_content)
            return Success(explosive_content)
        except Exception as e:
            session.rollback()
            return Failure(str(e))

def get_explosive_content():
    with session_maker() as session:
        return session.query(SuspiciousExplosiveContent.sentence).all()