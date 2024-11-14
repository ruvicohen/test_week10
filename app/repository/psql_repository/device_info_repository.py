from returns.result import Success, Failure, Result
from app.db.models import DeviceInfo
from app.db.psql_db import session_maker

def insert_device_info(device_info: DeviceInfo) -> Result[DeviceInfo, str]:
    with session_maker() as session:
        try:
            session.add(device_info)
            session.commit()
            session.refresh(device_info)
            return Success(device_info)
        except Exception as e:
            session.rollback()
            return Failure(str(e))