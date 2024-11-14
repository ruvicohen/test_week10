from returns.result import Result, Failure, Success

from app.db.models import Location
from app.db.psql_db import session_maker


def insert_location(location: Location) -> Result[Location, str]:
    with session_maker() as session:
        try:
            session.add(location)
            session.commit()
            session.refresh(location)
            return Success(location)
        except Exception as e:
            session.rollback()
            return Failure(str(e))