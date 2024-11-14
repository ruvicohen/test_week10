from typing import Dict
from returns.maybe import Nothing, Some, Maybe
from toolz import pipe
from app.db.models import DeviceInfo
from app.repository.psql_repository.device_info_repository import insert_device_info
from app.utils.model_utils import has_all_keys

def create_device_info(device_info_dict: Dict[str, str]) -> DeviceInfo:
    return DeviceInfo(
        browser=device_info_dict["browser"],
        os=device_info_dict["os"],
        device_id=device_info_dict["device_id"],
    )

def extract_device_info_from_json(device_info_json):
    return {
        "browser": device_info_json["latitude"],
        "os": device_info_json["longitude"],
        "device_id": device_info_json["city"]
    }

def convert_to_device_info(device_info_json: Dict[str, str]) -> Maybe[DeviceInfo]:
    return pipe(
        device_info_json,
        has_all_keys(['browser', 'os', 'device_id']),
        lambda is_valid: Nothing if not is_valid else Some(create_device_info(device_info_json))
    )

def create_device_info_service(device_info_json):
    return Maybe.from_optional(device_info_json).bind(convert_to_device_info).bind(insert_device_info)