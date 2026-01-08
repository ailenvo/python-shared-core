from datetime import datetime, timedelta
import uuid
from core.constants import constant
from uuid6 import uuid7
from bson import Binary


def new_uuid_v7_binary() -> Binary:
    return Binary(uuid7().bytes, subtype=4)


def str_id_to_binary_id(id: str) -> Binary:
    u = uuid.UUID(id)  # parse UUID string
    return Binary(u.bytes, subtype=4)


def binary_id_to_str(binary_id: Binary) -> str:
    return str(uuid.UUID(bytes=binary_id))


def convert_timestamp_to_str_vn(timestamp: float) -> str:
    """Chuyển timestamp epoch thành chuỗi định dạng ISO 8601 (2025-05-28T15:46:13+07:00)."""
    if timestamp is None:
        return None
    dt = datetime.fromtimestamp(timestamp).astimezone(constant.VN_TIMEZONE)
    return dt.strftime("%Y-%m-%dT%H:%M:%S+07:00")


def convert_timestamp_to_str_day_vn(timestamp: float) -> str:
    """Chuyển timestamp epoch thành chuỗi định dạng ISO 8601 (2025-05-28)."""
    if timestamp is None:
        return None
    dt = (
        datetime.fromtimestamp(timestamp)
        .astimezone(constant.VN_TIMEZONE)
        .strftime("%d-%m-%Y")
    )
    return dt


def timestamp_to_datetime_vn(timestamp: float) -> datetime:
    if timestamp is None:
        return None
    dt = datetime.fromtimestamp(timestamp).astimezone(constant.VN_TIMEZONE)
    return dt


def begin_timestamp_of_day(value):
    date_object = datetime.fromtimestamp(value).astimezone(constant.VN_TIMEZONE)
    date_object = date_object.replace(hour=0, minute=0, second=0, microsecond=0)
    return int(date_object.timestamp())


def safe_date_replace(dt: datetime, year, month):
    day = dt.day
    # số ngày tối đa của tháng trước
    last_day = (
        (datetime(year, month + 1, 1) - timedelta(days=1)).day if month != 12 else 31
    )
    day = min(day, last_day)
    return dt.replace(year=year, month=month, day=day)


def percentage_change(current_value: float, compare_value: float) -> float:
    if current_value == -1:
        current_value = 0
    if (compare_value == 0 and current_value == 0) or compare_value == current_value:
        return 0
    if compare_value == 0:
        return 100
    return round(((current_value - compare_value) / compare_value) * 100, 2)


def percentage(current_value: float, compare_value: float) -> float:
    if current_value == -1 or compare_value == 0:
        current_value = 0
    if (compare_value == 0 and current_value == 0) or compare_value == current_value:
        return 100
    return round(((current_value - compare_value) / compare_value) * 100, 2)
