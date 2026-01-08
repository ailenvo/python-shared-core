class AuthError(Exception):
    pass


class InvalidTokenError(AuthError):
    pass


class ExpiredTokenError(AuthError):
    pass


class PermissionDeniedError(AuthError):
    pass
