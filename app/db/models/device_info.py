from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.db.psql_db import Base


class DeviceInfo(Base):
    __tablename__ = "device_info"
    device_info_id = Column(Integer, primary_key=True, autoincrement=True)
    browser = Column(String)
    os = Column(String)
    device_id = Column(String)

    user_quote = relationship("UserQuote", back_populates="device_info", uselist=False)