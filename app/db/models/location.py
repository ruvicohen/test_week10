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

    user_quote = relationship("UserQuote", back_populates="location", uselist=False)