def create_suspicious_hostage_content(content_dict: Dict[str, str]) -> SuspiciousHostageContent:
    return SuspiciousHostageContent(
        sentence=content_dict["sentence"],
        user_quote_id=content_dict["user_quote_id"]
    )


def convert_to_suspicious_hostage_content(content_json: Dict[str, str]) -> Maybe[SuspiciousHostageContent]:
    return pipe(
        content_json,
        has_all_keys(['sentence', 'user_quote_id']),
        lambda is_valid: Nothing if not is_valid else Some(create_suspicious_hostage_content(content_json))
    )