from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.psql_db import Base


class UserQuote(Base):
    __tablename__ = "user_quote"
    user_quote_id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String)
    email = Column(String)
    ip_address = Column(String)
    created_at = Column(String)

    location_id = Column(Integer, ForeignKey("location.location_id"))
    device_info_id = Column(Integer, ForeignKey("device_info.device_info_id"))

    location = relationship("Location", back_populates="user_quote")
    device_info = relationship("DeviceInfo", back_populates="user_quote")
    sentences_explosive = relationship("SuspiciousExplosiveContent", back_populates="user_quote")
    sentences_hostage = relationship("SuspiciousHostageContent", back_populates="user_quote")