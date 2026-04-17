import telebot
import os
import time  # Importamos la librería de tiempo para hacer la pausa

TOKEN = os.environ.get('TOKEN')
bot = telebot.TeleBot(TOKEN)

def obtener_primera_linea(texto):
    if not texto: return "Sin título"
    for linea in texto.splitlines():
        linea = linea.strip()
        if linea: return linea
    return "Sin título"

@bot.message_handler(content_types=['video', 'document'])
def procesar_mensajes(message):
    # La pausa de seguridad: el bot espera 1 segundo antes de empezar a procesar
    # Esto asegura que si envías 20, los procese con calma, uno tras otro.
    time.sleep(1) 
    
    texto = message.caption
    nueva_descripcion = obtener_primera_linea(texto)
    
    if message.content_type == 'video':
        bot.send_video(message.chat.id, message.video.file_id, caption=nueva_descripcion)
    elif message.content_type == 'document':
        bot.send_document(message.chat.id, message.document.file_id, caption=nueva_descripcion)

if __name__ == '__main__':
    bot.infinity_polling(skip_pending=True)
