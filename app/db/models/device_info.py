from sqlalchemy import Column, String, Integer

from app.db.psql_db import Base


class DeviceInfo(Base):
    device_info_id = Column(Integer, primary_key=True, autoincrement=True)
    browser = Column(String)
    os = Column(String)
    device_id = Column(String)