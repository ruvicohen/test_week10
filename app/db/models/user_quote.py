from sqlalchemy import Column, Integer, String
from app.db.psql_db import Base


class UserQuote(Base):
    user_quote_id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String)
    email = Column(String)
    ip_address = Column(String)
    created_at = Column(String)
    location = Column(String)
    device_info = Column(String)
    sentences = Column(String)