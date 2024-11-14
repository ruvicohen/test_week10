from returns.maybe import Maybe
from returns.result import Result, Success, Failure
from app.db.models import UserQuote
from app.db.psql_db import session_maker


def insert_user_quote(user_quote: UserQuote) -> Result[UserQuote, str]:
    with session_maker() as session:
        try:
            session.add(user_quote)
            session.commit()
            session.refresh(user_quote)
            return Success(user_quote)
        except Exception as e:
            session.rollback()
            return Failure(str(e))

def get_user_quote_by_id(user_quote_id: int) -> Maybe[UserQuote]:
    with session_maker() as session:
        return Maybe.from_optional(session.query(UserQuote)
                            .filter(UserQuote.user_quote_id == user_quote_id).first())
