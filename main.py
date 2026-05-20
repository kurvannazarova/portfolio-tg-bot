import telebot
# import os
# from dotenv import load_dotenv


# load_dotenv()

BOT_TOKEN = "8930768015:AAEjPp0oOmDIxSR1r5KVfQrii-aTnAg9ZT4"
bot = telebot.TeleBot(BOT_TOKEN, parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Assalom alaykum, botga xush kelibsiz")
	
@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, message.text)
	
bot.infinity_polling()

