import telebot
from telebot import types
import os
from dotenv import load_dotenv


load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN, parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    text = "Assalom alaykum👋🏻, botga xush kelibsiz! Men Kurvannazarova Dilmira kichik frontend dasturchiman👩🏻‍💻."
	# bot.reply_to(message, "Assalom alaykum👋🏻, botga xush kelibsiz! Men Kurvannazarova Dilmira kichik frontend dasturchiman👩🏻‍💻." )
    keyboard = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton("About me")
    btn2 = types.KeyboardButton("Contact")
    keyboard.add(btn1, btn2)
    bot.send_message(message.chat.id, text, reply_markup = keyboard )
	
@bot.message_handler(func=lambda m: True)
def echo_all(message):
	if message.text =="Abut me":
		bot.send_message(message.chat.id, "Men Kurvannazarova Dilmira...")
	elif message.text == "Contact":
		bot.send_message(message.chat.id, "Tez orada qo'shiladi😁")
	
bot.infinity_polling()
