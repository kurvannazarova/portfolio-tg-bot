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
    keyboard = types.ReplyKeyboardMarkup()
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
        "About me\n"
        "Hi everyone! I'm Dilmira Kurvannazarova.\n"
        "I'm a student studying at IT Park, and I'm 15 years old.\n"
        "I live in Shovot, Khorezm, where I pursue my passion for learning and creativity.\n"
        "My hobbies include listening to music, reading books, and writing stories. "
        "These activities fuel my imagination and help me express myself creatively.\n"
        "I'm deeply interested in literature, my mother tongue, English, and history. "
        "These subjects inspire me to explore different perspectives and understand the world around me."
    )
    bot.send_message(message.chat.id, text)

@bot.message_handler(func=lambda message: message.text == "Contact")
def contact_handler(message):
    text = "Tap to button to contact me"
    keyboard = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Telegram", url="https://t.me/gulmira_12_09")
    keyboard.add(btn1)
    bot.send_message(message.chat.id, text, reply_markup=keyboard)
    
def aboutme_handler(message):
    text = (
        "Will be added soon"
    )
    bot.send_message(message.chat.id, text)

bot.infinity_polling()

