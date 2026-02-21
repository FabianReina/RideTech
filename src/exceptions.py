# exceptions.py

class UserAlreadyExistsError(Exception):
    pass


class InvalidDataError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class RouteError(Exception):
    pass