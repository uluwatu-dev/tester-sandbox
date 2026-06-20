import re
from datetime import datetime
from zoneinfo import ZoneInfo

def convert_local_to_utc(date_str: str, local_tz_name: str) -> datetime:
    """
    Converts a local date string (e.g., '2026-06-20 15:30:00') in a given timezone to UTC.
    """
    naive_dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    local_tz = ZoneInfo(local_tz_name)
    local_dt = naive_dt.replace(tzinfo=local_tz)
    return local_dt.astimezone(ZoneInfo("UTC"))

def validate_email(email: str) -> bool:
    """
    Validates email format using standard regex.
    """
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))

def add_numbers(a: int, b: int) -> int:
    """
    Basic addition helper.
    """
    return a + b
