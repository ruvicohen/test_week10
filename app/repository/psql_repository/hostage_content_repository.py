from typing import List
from returns.result import Result, Failure, Success
from app.db.models import SuspiciousHostageContent
from app.db.psql_db import session_maker
from app.repository.psql_repository.user_quote_repository import get_user_quote_by_id

def insert_hostage_content(hostage_content: SuspiciousHostageContent) \
        -> Result[SuspiciousHostageContent, str]:
    with session_maker() as session:
        try:
            user_quote_id = hostage_content.user_quote_id
            if get_user_quote_by_id(user_quote_id).value_or(None) is None:
                return Failure("user quote not found")
            session.add(hostage_content)
            session.commit()
            session.refresh(hostage_content)
            return Success(hostage_content)
        except Exception as e:
            session.rollback()
            return Failure(str(e))

def get_hostage_content() -> List[str]:
    with session_maker() as session:
        return session.query(SuspiciousHostageContent.sentence).all()