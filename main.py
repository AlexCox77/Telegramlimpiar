# main.py

import telebot

# Reemplaza 'AQUI_TU_TOKEN' por el token de tu bot de Telegram
TOKEN = 'AQUI_TU_TOKEN'

bot = telebot.TeleBot(TOKEN)

def obtener_primera_linea(texto):
    """Devuelve la primera línea no vacía del texto recibido."""
    if not texto:
        return ""
    # Separa por saltos de línea, quita espacios y devuelve la primera línea no vacía
    for linea in texto.splitlines():
        linea = linea.strip()
        if linea:
            return linea
    return ""

@bot.message_handler(content_types=['text', 'photo', 'video', 'document'])
def responder_con_primera_linea(message):
    texto = message.text or message.caption
    primera_linea = obtener_primera_linea(texto)
    if primera_linea:
        bot.reply_to(message, primera_linea)
    else:
        # Si no hay texto ni caption, no devuelve nada
        pass

if __name__ == '__main__':
    # Importante para que funcione correctamente en entornos tipo Render/server
    bot.infinity_polling(skip_pending=True)
