from sqlalchemy import Column, Integer, String
from app.db.psql_db import Base


class Location(Base):
    location_id = Column(Integer, primary_key=True, autoincrement=True)
    latitude = Column(Integer)
    longitude = Column(Integer)
    city = Column(String)
    country = Column(String)