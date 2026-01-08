# core/auth/jwt.py
from datetime import datetime, timedelta
from jose import jwt, JWTError
from typing import Dict, Any

from auth.exceptions import InvalidTokenError, ExpiredTokenError
from schemas.base import AuthUser

ALGORITHM = "HS256"


def create_access_token(
    payload: AuthUser,
    secret_key: str,
    expires_minutes: int = 30,
) -> str:
    data = payload.dict(exclude_none=True)
    expire = datetime.utcnow() + timedelta(minutes=expires_minutes)
    data.update({"exp": expire})

    return jwt.encode(data, secret_key, algorithm=ALGORITHM)


def decode_token(token: str, secret_key: str) -> AuthUser:
    try:
        payload: Dict[str, Any] = jwt.decode(
            token,
            secret_key,
            algorithms=[ALGORITHM],
        )

        return AuthUser(
            tenant_id=payload.get("tenant_id"),
            user_id=payload.get("user_id"),
            email=payload.get("email"),
            role=payload.get("role"),
        )

    except jwt.ExpiredSignatureError:
        raise ExpiredTokenError("Token expired")

    except JWTError:
        raise InvalidTokenError("Invalid token")
