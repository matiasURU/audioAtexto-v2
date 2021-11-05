import requests

from web.servicios import rest_api


def validar_credenciales(usuario, correo, clave):
    body = {"nombre": usuario,
            "correo": correo,
            "clave": clave,
            "rol": "administrador"}
    respuesta = requests.post(f'{rest_api.API_URL}/login', json=body)
    return respuesta.status_code == 200


def crear_usuario(usuario, correo, clave):
    body = {"nombre": usuario,
            "correo": correo,
            "clave": clave,
            "rol": "cliente"}
    respuesta = requests.post(f'{rest_api.API_URL}/usuarios', json=body)
    return respuesta.status_code == 200


def obtener_usuarios():
    respuesta = requests.get(f'{rest_api.API_URL}/usuarios')
    return respuesta.json()
