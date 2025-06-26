import telebot
import yt_dlp
import os
import re

from dotenv import load_dotenv

load_dotenv()
bot = telebot.TeleBot(os.getenv("BOT_TOKEN"))

def sanitize_filename(filename):
    return re.sub(r'[\\/*?:"<>|]', '', filename)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Hello! Send me a YouTube link and I will convert it to an audio file for you 🎵')

@bot.message_handler(func=lambda message: True)
def link(message):
    link_yt = message.text.strip()

    if 'youtube.com' in link_yt or 'youtu.be' in link_yt:
        bot.reply_to(message, "Processing your request, please wait a moment...")

        try:
            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '320',
                }],
                'outtmpl': '%(title)s.%(ext)s',
                'quiet': True,
                'ffmpeg_location': r'C:\ffmpeg\bin',
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(link_yt, download=True)
                title = sanitize_filename(info_dict['title'])
                filename = f"{title}.mp3"

            if os.path.exists(filename):
                with open(filename, 'rb') as audio:
                    bot.send_audio(message.chat.id, audio, caption=f"Here is your audio: {title} 🎵")

                os.remove(filename)

        except Exception as e:
            bot.reply_to(message, f"An error occurred: {e}")

    else:
        bot.reply_to(message, "Please send a valid YouTube video link.")

bot.polling()
