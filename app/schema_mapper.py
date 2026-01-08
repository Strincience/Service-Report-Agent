def normalize_keys(row: dict) -> dict:
    """
    Strip whitespace from all keys in a Google Form response row.
    """
    return {key.strip(): value for key, value in row.items()}

def safe_get(row, key, default=None):
    """
    Safely get a value from a dictionary, stripping whitespace and providing a default."""
    value = row.get(key, default)
    if isinstance(value, str):
        value = value.strip()
    return value or default


def to_int(value):
    """
    Docstring for to_int
    Convert a value to an integer, returning 0 if conversion fails.
    """
    try:
        return int(value)
    except (TypeError, ValueError):
        return 0
    


def map_row_to_report_schema(raw_row: dict) -> dict:
    row = normalize_keys(raw_row)

    return {
        "heading": {
            "service_date": safe_get(row, "Date of Service"),
            "service_theme": safe_get(row, "Theme"),
            "start_time": safe_get(row, "Start Time"),
            "venue": safe_get(row, "Venue")
        },

        "workers_charge": {
            "opening_time": safe_get(row, "Opening time"),
            "opening_prayer_and_worship": safe_get(row, "Opening Prayer & Worship Time"),
            "sessions_and_facilitators": safe_get(row, "Sessions & Facilitators"),
            "key_highlights": safe_get(row, "Key Highlights from the Charge")
        },

        "service_outline": {
            "order_of_service": safe_get(row, "Order of Service (chronological)")
        },

        "sermon": {
            "preacher": safe_get(row, "Name of the Preacher"),
            "topic": safe_get(row, "Sermon Topic"),
            "scriptures": safe_get(row, "Bible Text(s)"),
            "main_thought": safe_get(row, "Main Thought of the Message"),
            "key_points": safe_get(row, "Key Points from the Message")
        },

        "attendance": {
            "male": to_int(safe_get(row, "Number of Male Attendees")),
            "female": to_int(safe_get(row, "Number of Female Attendees")),
            "total": (
                to_int(safe_get(row, "Number of Male Attendees")) +
                to_int(safe_get(row, "Number of Female Attendees"))
            )
        },

        "challenges": {
            "had_challenges": safe_get(row, "Were There Any Challenges?"),
            "description": safe_get(row, "Describe the Challenges Encountered")
        },

        "authorship": {
            "prepared_by": safe_get(row, "Name of report preparer"),
            "role": safe_get(row, "Role / Unit"),
            "timestamp": safe_get(row, "Timestamp")
        }
    }

