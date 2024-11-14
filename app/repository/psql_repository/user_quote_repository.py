from returns.maybe import Maybe
from returns.result import Result, Success, Failure
from app.db.models import UserQuote, Location, DeviceInfo, SuspiciousExplosiveContent, SuspiciousHostageContent
from app.db.psql_db import session_maker
from sqlalchemy.exc import NoResultFound

from app.utils.model_utils import convert_user_quote_to_json


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

def get_user_quote_with_all_by_email(email: str) -> Maybe[UserQuote]:
    with session_maker() as session:
        return Maybe.from_optional(session.query(UserQuote)
                            .filter(UserQuote.email == email).all())

def get_user_data_by_email(email: str):
    with session_maker() as session:
        try:
            user_quote = session.query(UserQuote).filter(UserQuote.email == email).one()
            result = {
                "email": user_quote.email,
                "username": user_quote.username,
                "ip_address": user_quote.ip_address,
                "created_at": user_quote.created_at,
                "location": {
                    "latitude": user_quote.location.latitude,
                    "longitude": user_quote.location.longitude,
                    "city": user_quote.location.city,
                    "country": user_quote.location.country,
                } if user_quote.location else None,
                "device_info": {
                    "browser": user_quote.device_info.browser,
                    "os": user_quote.device_info.os,
                    "device_id": user_quote.device_info.device_id,
                } if user_quote.device_info else None,
                "sentences": [
                    content.sentence for content in user_quote.sentences_explosive
                ] + [
                    content.sentence for content in user_quote.sentences_hostage
                ],
            }
            return result
        except NoResultFound:
            return None

def get_user_data_by_email1(email):
    with session_maker() as session:
        user_data = (
            session.query(
                UserQuote
            )
            .join(Location, UserQuote.location_id == Location.location_id, isouter=True)
            .join(DeviceInfo, UserQuote.device_info_id == DeviceInfo.device_info_id, isouter=True)
            .outerjoin(SuspiciousExplosiveContent, UserQuote.user_quote_id == SuspiciousExplosiveContent.user_quote_id)
            .outerjoin(SuspiciousHostageContent, UserQuote.user_quote_id == SuspiciousHostageContent.user_quote_id)
            .filter(UserQuote.email == email)
            .first()
        )

        if not user_data:
            return None

        return convert_user_quote_to_json(user_data)