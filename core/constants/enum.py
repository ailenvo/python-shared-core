from enum import Enum


class HEADER(str, Enum):
    ApiKey = "x-api-key"
    AcceptLanguage = "accept-language"
    Authorization = "authorization"
    InternalToken = "X-Internal-Token"


class LANGUAGE_CODES(str, Enum):
    VI = "vn"
    EN = "en"


class COOKIE(str, Enum):
    RefetchToken = "x-rtoken"


class OBJECT_STATUS(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    IS_DELETED = "delete"
