import pytest

from src.users import (
    registrar_usuario,
    login,
    usuarios
)

from src.exceptions import (
    UserAlreadyExistsError,
    InvalidDataError,
    AuthenticationError
)


def setup_function():
    usuarios.clear()


def test_registro_correcto():

    user = registrar_usuario(
        "Juan",
        "juan@test.com",
        "1234"
    )

    assert user["email"] == "juan@test.com"


def test_password_corta():

    with pytest.raises(InvalidDataError):
        registrar_usuario("Ana", "ana@test.com", "12")


def test_usuario_duplicado():

    registrar_usuario("A", "a@test.com", "1234")

    with pytest.raises(UserAlreadyExistsError):
        registrar_usuario("B", "a@test.com", "9999")


def test_login_correcto():

    registrar_usuario("Luis", "l@test.com", "abcd")

    user = login("l@test.com", "abcd")

    assert user["nombre"] == "Luis"


def test_login_usuario_no_existe():

    with pytest.raises(AuthenticationError):
        login("x@test.com", "1234")


def test_login_password_incorrecta():

    registrar_usuario("Ana", "ana@test.com", "abcd")

    with pytest.raises(AuthenticationError):
        login("ana@test.com", "9999")