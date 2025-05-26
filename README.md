# 🤖 Simple Aiogram Echo Bot

This repository contains a minimal Telegram bot built using [Aiogram](https://github.com/aiogram/aiogram), an asynchronous Python framework for Telegram Bot API.

The bot simply echoes any message it receives.

## ✨ Features

- Replies with the same text as received (echo functionality)
- Uses environment variables for configuration (via `.env`)
- Organized using routers and dispatcher for extensibility

## ⚙️ Requirements

- Python 3.8+
- [Aiogram](https://pypi.org/project/aiogram/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

## 🚀 Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/edgerunn3r21/echo-telegram-bot
   cd echo-telegram-bot
   ```

2. **Create a virtual environment**

   ```bash
   python3 -m venv .venv
   ```

3. **Activate the virtual environment**

   ```bash
   # For Windows:
   .venv\Scripts\activate

   # For Linux/MacOS:
   source .venv/bin/activate
   ```

4. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

5. **Set up your environment variables:**

   Create a `.env` file in the root directory with your Telegram bot token (Example in the file .env.example):

   ```
   token=YOUR_TELEGRAM_BOT_TOKEN
   ```

## ▶️ Usage

Run the bot with:

```bash
python main.py
```

## 🗂️ Project Structure

```
yourbotrepo/
│
├── .env                # Environment variables (not included in repo, only .env.example)
├── requirements.txt    # Python dependencies
├── your_bot_script.py  # Main bot script
└── README.md           # This file
```

## 🛠️ How It Works

- Loads the bot token from `.env`
- Initializes the Aiogram `Bot`, `Dispatcher`, and a simple message router
- Defines a message handler that echoes incoming messages
- Starts polling and responding to updates

## ☕ Support the Author

If you found this bot or repository useful, you can support the author:

[![Support me on Ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/satori_code)