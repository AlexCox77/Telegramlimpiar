import telebot
import os

TOKEN = os.environ.get('TOKEN')
bot = telebot.TeleBot(TOKEN)

def obtener_primera_linea(texto):
    if not texto:
        return ""
    for linea in texto.splitlines():
        linea = linea.strip()
        if linea:
            return linea
    return ""

@bot.message_handler(content_types=['text', 'photo', 'video', 'document'])
def responder_con_primera_linea(message):
    # Intentamos obtener el texto del mensaje actual
    # Si es un reenvío, intentamos sacar el caption del mensaje original
    texto = message.text or message.caption
    
    # Si sigue vacío y es un reenvío, buscamos en el mensaje original (forward)
    if not texto and message.forward_from_chat:
        texto = message.caption
        
    primera_linea = obtener_primera_linea(texto)
    
    if primera_linea:
        bot.reply_to(message, primera_linea)

if __name__ == '__main__':
    bot.infinity_polling(skip_pending=True)
    
