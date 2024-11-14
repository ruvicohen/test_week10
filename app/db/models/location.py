from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.psql_db import Base


class Location(Base):
    __tablename__ = "location"
    location_id = Column(Integer, primary_key=True, autoincrement=True)
    latitude = Column(Integer)
    longitude = Column(Integer)
    city = Column(String)
    country = Column(String)

    user_quote_id = Column(Integer, ForeignKey("user_quote.user_quote_id"))

    user_quote = relationship("UserQuote", back_populates="user_quotes")