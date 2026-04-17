import telebot
import os

# 1. Obtenemos el token desde las variables de entorno de Render
# Esto es mucho más seguro que escribir el token directamente aquí
TOKEN = os.environ.get('TOKEN')

# Creamos la instancia del bot
bot = telebot.TeleBot(TOKEN)

def obtener_primera_linea(texto):
    """Devuelve la primera línea no vacía del texto recibido."""
    if not texto:
        return ""
    # Separa por saltos de línea y toma la primera parte con contenido
    for linea in texto.splitlines():
        linea = linea.strip()
        if linea:
            return linea
    return ""

@bot.message_handler(content_types=['text', 'photo', 'video', 'document'])
def responder_con_primera_linea(message):
    # Extraemos el texto (si es mensaje normal) o la descripción (si es archivo)
    texto = message.text or message.caption
    
    # Obtenemos la línea limpia usando la función
    primera_linea = obtener_primera_linea(texto)
    
    if primera_linea:
        # Respondemos al usuario con la línea limpia
        bot.reply_to(message, primera_linea)

if __name__ == '__main__':
    print("Bot encendido y escuchando...")
    # infinity_polling mantiene el bot activo esperando mensajes
    bot.infinity_polling(skip_pending=True)
    
