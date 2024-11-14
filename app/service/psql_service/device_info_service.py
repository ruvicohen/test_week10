def create_device_info(device_info_dict: Dict[str, str]) -> DeviceInfo:
    return DeviceInfo(
        browser=device_info_dict["browser"],
        os=device_info_dict["os"],
        device_id=device_info_dict["device_id"],
        user_quote_id=device_info_dict["user_quote_id"]
    )


def convert_to_device_info(device_info_json: Dict[str, str]) -> Maybe[DeviceInfo]:
    return pipe(
        device_info_json,
        has_all_keys(['browser', 'os', 'device_id', 'user_quote_id']),
        lambda is_valid: Nothing if not is_valid else Some(create_device_info(device_info_json))
    )