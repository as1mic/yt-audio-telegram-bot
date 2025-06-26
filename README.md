# YouTube MP3 Telegram Bot

This is a simple Telegram bot written in **Python** that downloads YouTube videos as **high-quality MP3 audio files** and sends them back to the user.

---

## Features

- Supports YouTube video links
- Converts to 320kbps MP3 using **yt-dlp** and **FFmpeg**
- Sends audio file directly in the chat
- Automatically deletes temporary files after sending
- Uses `.env` file to store the bot token securely

---

## Technologies Used

- Python 3
- [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI)
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- FFmpeg (for audio conversion)
- python-dotenv (for managing secrets)

---

## How to Run

1. **Clone the repository**:

```bash
git clone https://github.com/as1mic/yt-audio-telegram-bot.git
cd yt-audio-telegram-bot
```

2. **Create a virtual environment (optional but recommended)**:

```bash
python -m venv venv
venv\Scripts\activate   # On Windows
source venv/bin/activate  # On Linux/macOS
```

3. **Install dependencies**:

```bash
pip install -r requirements.txt
```

4. **Install [FFmpeg](https://ffmpeg.org/download.html)** and note the path (e.g., `C:/ffmpeg/bin`).

5. **Create a `.env` file** in the project root:

```
BOT_TOKEN=your_telegram_bot_token
```

6. **Run the bot**:

```bash
python main.py
```

---

## Example Usage

Just send the bot a YouTube link like:

```
https://youtu.be/dQw4w9WgXcQ
```

And it will reply with the MP3 audio 🎧

---

## Disclaimer

This bot is for **educational purposes only**. Downloading copyrighted content may violate YouTube's terms of service.

---

## Author

Asim Aliiev