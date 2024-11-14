from returns.result import Result, Success, Failure

from app.db.mongo_db import all_messages


def insert_email(email: dict) -> Result[dict, str]:
    try:
        all_messages.insert_one(email)
        return Success(email)
    except Exception as e:
        return Failure(str(e))
