import telebot
from telebot import types
import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN, parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    text = "Good day👋🏻, welcome to my bot! I am Kurvannazarova Dilmira, a small frontend developer👩🏻‍💻."
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("About me")
    btn2 = types.KeyboardButton("Contact")
    btn3 = types.KeyboardButton("Skills")
    btn4 = types.KeyboardButton("Projects")
    keyboard.add(btn1, btn2)
    keyboard.add(btn3, btn4)
    bot.send_message(message.chat.id, text, reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == "About me")
def aboutme_handler(message):
    text = (
        "About Me 🌟\n"
        "Hi everyone! I'm Dilmira Kurvannazarova 👋\n"
        "I'm a 15-year-old student at IT Park 👩🏻‍💻 and I live in Shovot, Khorezm 🌍.\n"
        "I love learning and being creative ✨. My hobbies are listening to music 🎧, reading books 📚, and writing stories ✍️.\n"
        "I'm interested in literature, languages (especially English), and history 📖 — they help me see the world in a deeper way 🌎."
    )
    bot.send_message(message.chat.id, text)

@bot.message_handler(func=lambda message: message.text == "Contact")
def contact_handler(message):
    text = "Tap to button to contact me"
    keyboard = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Telegram", url="https://t.me/gulmira_12_09")
    keyboard.add(btn1)
    bot.send_message(message.chat.id, text, reply_markup=keyboard)
    
@bot.message_handler(func=lambda message: message.text == "Skills")
def skills_handler(message):
    text = (
        "Will be added soon"
    )
    bot.send_message(message.chat.id, text)

@bot.message_handler(func=lambda message: message.text == "Projects")
def projects_handler(message):
    text = (
        "My projects \n"
        "From cryllic to latin, from latin to cryllic bot [Bot link](@LotinKrilSimpleBot )\n"
    )
    bot.send_message(message.chat.id, text)

bot.infinity_polling()

