import telebot
import os
from dotenv import load_dotenv


load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN, parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Assalom alaykum👋🏻, botga xush kelibsiz!" \
	"Men Kurvannazarova Dilmira kichik frontend dasturchiman👩🏻‍💻")
	
# @bot.message_handler(func=lambda m: True)
# def echo_all(message):
# 	bot.reply_to(message, message.text)
	
bot.infinity_polling()

