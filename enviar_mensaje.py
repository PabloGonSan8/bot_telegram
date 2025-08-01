"""
Pasos a realizar:
1. Crear un bot en Telegram con botfather y obtener el TOKEN.
2. Crear un archivo llamado variables.py y definir la variable TOKEN con el token del bot.
3. Enviar un mensaje al bot para que se registre el chat_id.
4. Ejecutar el script desde la terminal con el comando: python -u (nombre_del_script).py
5. Ingresar el mensaje que se desea enviar al bot.
"""
import requests
# CONFIGURACIÓN
# Se debe crear un archivo variales.py con el TOKEN del bot de Telegram
from variables import TOKEN,CHAT_ID
# Con esta funcion se obtiene el chat_id del bot de Telegram
"""
def get_chat_id():
    try:
        return print(requests.get(f"https://api.telegram.org/bot{TOKEN}/getUpdates").json()['result'][0]['message']['chat']['id'])
    except Exception as e:
        print(f"Error al obtener el chat_id: {e}")
        return None
"""
# Lanzamos la peticion a la API de Telegram para enviar un mensaje
# Se utilizan los parametros chat_id (obtenido anteriormente) y text (el mensaje a enviar)
def enviar_mensaje_telegram(texto):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    params = {
        "chat_id": CHAT_ID,
        "text": texto
    }
    try:
        requests.get(url, params=params)
        print("Mensaje enviado correctamente.")
    except Exception as e:
        print(f"Error al enviar el mensaje: {e}")
    
# LLamamos a la funcion pasando el mensaje por parametro
# Lanzamos el comando en la terminal python -u enviar_mensaje.py
enviar_mensaje_telegram(input("Escribe el mensaje que quieres enviar: "))