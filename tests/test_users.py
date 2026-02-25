import pytest
from src.users import registrar_usuario, autenticar_usuario, usuarios




def test_registro_normal():
    usuarios.clear() # Mantén la casa limpia
    usuario = registrar_usuario("nico", "1234")
    assert usuario["username"] == "nico"
    assert usuario["password"] == "1234"

def test_registro_username_nulo():
    usuarios.clear()
    usuario = registrar_usuario(None, "1234")
    assert usuario["username"] == "usuario_default"

def test_registro_password_nulo():
    usuarios.clear()
    usuario = registrar_usuario("nico2", None)
    assert usuario["password"] == "123456"

def test_autenticacion_correcta():
    usuarios.clear()
    registrar_usuario("testuser", "abc")
    assert autenticar_usuario("testuser", "abc") is True

def test_autenticacion_incorrecta():
    usuarios.clear()
    assert autenticar_usuario("noexiste", "123") is False

def test_no_permitir_usuarios_duplicados():
    usuarios.clear() 
    
    # Registramos un usuario por primera vez
    registrar_usuario("user123", "pass1")
    assert len(usuarios) == 1
    
    # Intentamos registrar el MISMO username con otra contraseña
    registrar_usuario("user123", "pass2")
    
    # VALIDACIÓN: La lista NO debe haber crecido, debe seguir en 1
    assert len(usuarios) == 1
    
    # VALIDACIÓN EXTRA: El password debe seguir siendo el del primer registro
    assert usuarios[0]["password"] == "pass1"

def test_registro_multiples_usuarios_distintos():
    usuarios.clear()
    registrar_usuario("nico", "1234")
    registrar_usuario("camilo", "32222")
    registrar_usuario("camilo", "32222")
    
    # Aquí sí deben haber 3, porque son diferentes
    assert len(usuarios) == 3