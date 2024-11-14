from typing import Dict
from returns.maybe import Nothing, Some, Maybe
from toolz import pipe
from app.db.models import Location
from app.repository.psql_repository.location_repository import insert_location
from app.utils.model_utils import has_all_keys

def create_location(location_dict: Dict[str, str]) -> Location:
    return Location(
        latitude=location_dict["latitude"],
        longitude=location_dict["longitude"],
        city=location_dict["city"],
        country=location_dict["country"],
    )

def extract_location_from_json(location_json: Dict[str, str]):
    return {
        "latitude": location_json["latitude"],
        "longitude": location_json["longitude"],
        "city": location_json["city"],
        "country": location_json["country"],
    }

def convert_to_location(location_json: Dict[str, str]) -> Maybe[Location]:
    return pipe(
        location_json,
        has_all_keys(['latitude', 'longitude', 'city', 'country']),
        lambda is_valid: Nothing if not is_valid else Some(create_location(location_json))
    )

def create_location_service(location_json):
    return Maybe.from_optional(location_json).bind(convert_to_location).bind(insert_location)