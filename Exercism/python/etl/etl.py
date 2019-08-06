def transform(legacy_data: dict) -> dict:
    """Transform legacy_data in new format"""
    return {v.lower(): key for key, value in legacy_data.items()
                           for v in value}
