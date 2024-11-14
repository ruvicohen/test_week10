def create_user_quote(user_quote_dict: Dict[str, str]) -> UserQuote:
    return UserQuote(
        username=user_quote_dict["username"],
        email=user_quote_dict["email"],
        ip_address=user_quote_dict["ip_address"],
        created_at=user_quote_dict["created_at"],
        location_id=user_quote_dict["location_id"],
        device_info_id=user_quote_dict["device_info_id"]
    )


def convert_to_user_quote(user_quote_json: Dict[str, str]) -> Maybe[UserQuote]:
    return pipe(
        user_quote_json,
        has_all_keys(['username', 'email', 'ip_address', 'created_at', 'location_id', 'device_info_id']),
        lambda is_valid: Nothing if not is_valid else Some(create_user_quote(user_quote_json))
    )