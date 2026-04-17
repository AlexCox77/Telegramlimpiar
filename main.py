import telebot
import os

TOKEN = os.environ.get('TOKEN')
bot = telebot.TeleBot(TOKEN)

def obtener_primera_linea(texto):
    if not texto: return "Sin título"
    for linea in texto.splitlines():
        linea = linea.strip()
        if linea: return linea
    return "Sin título"

@bot.message_handler(content_types=['video'])
def procesar_video(message):
    # Intentamos sacar el caption del reenvío
    texto = message.caption
    
    # Obtenemos la primera línea
    nueva_descripcion = obtener_primera_linea(texto)
    
    # Reenviamos el vídeo a ti mismo con la nueva descripción
    # message.chat.id es tu chat, message.video.file_id es el vídeo
    bot.send_video(
        chat_id=message.chat.id, 
        video=message.video.file_id, 
        caption=nueva_descripcion
    )

if __name__ == '__main__':
    bot.infinity_polling(skip_pending=True)
    
