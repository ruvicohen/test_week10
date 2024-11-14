def create_location(location_dict: Dict[str, str]) -> Location:
    return Location(
        latitude=location_dict["latitude"],
        longitude=location_dict["longitude"],
        city=location_dict["city"],
        country=location_dict["country"],
        user_quote_id=location_dict["user_quote_id"]
    )


def convert_to_location(location_json: Dict[str, str]) -> Maybe[Location]:
    return pipe(
        location_json,
        has_all_keys(['latitude', 'longitude', 'city', 'country', 'user_quote_id']),
        lambda is_valid: Nothing if not is_valid else Some(create_location(location_json))
    )