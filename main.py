import telebot
import os
import time
from flask import Flask
from threading import Thread

# --- Esto es lo que evita el error de la imagen ---
app = Flask('')

@app.route('/')
def home():
    return "Bot en línea"

def run():
    app.run(host='0.0.0.0', port=7860)

def keep_alive():
    t = Thread(target=run)
    t.start()
# --------------------------------------------------

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
    time.sleep(1) 
    texto = message.caption
    nueva_descripcion = obtener_primera_linea(texto)
    
    if message.content_type == 'video':
        bot.send_video(message.chat.id, message.video.file_id, caption=nueva_descripcion)
    elif message.content_type == 'document':
        bot.send_document(message.chat.id, message.document.file_id, caption=nueva_descripcion)

if __name__ == '__main__':
    keep_alive() # Arranca el servidor web para Hugging Face
    bot.infinity_polling(skip_pending=True)
    
