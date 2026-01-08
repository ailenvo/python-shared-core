from http import HTTPStatus
from typing import Generic, Optional, TypeVar
from datetime import datetime
from pydantic_core import core_schema
from pydantic import GetCoreSchemaHandler
from pydantic import BaseModel, Field
from typing import Any
from constants.enum import OBJECT_STATUS

T = TypeVar("T")


class AuthUser(BaseModel):
    tenant_id: Optional[str] = None
    user_id: Optional[str] = None
    email: Optional[str] = None
    role: Optional[str] = None


class AppBaseModels(BaseModel):
    created_at: Optional[datetime] = Field(default_factory=datetime.now)
    updated_at: Optional[datetime] = None
    created_by: Optional[str] = None
    updated_by: Optional[str] = None
    object_status: Optional[str] = OBJECT_STATUS.ACTIVE.value


class AppBaseModelRes(BaseModel):
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    created_by: Optional[str] = None
    updated_by: Optional[str] = None
    object_status: Optional[str] = OBJECT_STATUS.ACTIVE.value


class AppBaseResponse(BaseModel, Generic[T]):
    data: Optional[T] = None
    success: bool = True
    message: Optional[str] = ""
    status_code: int = HTTPStatus.OK
    error_code: Optional[int] = None
    timestamp: str = Field(default_factory=lambda: datetime.now().isoformat())


class AppBasePagingRes(BaseModel, Generic[T]):
    items: list[T] = []
    total: int = None
    is_full: bool = True
    page: Optional[int] = None
    page_size: Optional[int] = None


class BasePagingReq(BaseModel):
    keyword: Optional[str] = None
    page: Optional[int] = 1
    page_size: Optional[int] = 10
    object_status: Optional[str] = None
    all_items: Optional[bool] = False


class PhoneNumber(str):

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source_type: Any, handler: GetCoreSchemaHandler
    ) -> core_schema.CoreSchema:
        return core_schema.no_info_after_validator_function(
            cls.validate,
            core_schema.str_schema(),
        )

    @classmethod
    def validate(cls, v):
        # Example: Validate phone number format
        import re

        pattern = r"^\+?[1-9]\d{1,14}$"  # Simple phone number regex
        if not isinstance(v, str) or not re.match(pattern, v):
            raise ValueError("Invalid phone number")
        return v
