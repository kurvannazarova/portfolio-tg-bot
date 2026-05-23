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
	
# @bot.message_handler(func=lambda m: True)
# def echo_all(message):
# 	if message.text =="About me":
# 		bot.send_message(message.chat.id, "Men Kurvannazarova Dilmira...")
# 	elif message.text == "Contact":
# 		bot.send_message(message.chat.id, "Tez orada qo'shiladi😁")

@bot.message_handler(func=lambda message: message.text == "About me")
def aboutme_handler(message):
	bot.send_message(message.chat.id, "About me" "\n" " Hi everyone! I'm Dilmira Kurvannazarova." "\n" "I'm a student studying at IT Park, and I'm 15 years old."  "\n" "I live in Shovot, Khorezm, where I pursue my passion for learning and creativity." "\n" "My hobbies include listening to music, reading books, and writing stories. These activities fuel my imagination and help me express myself creatively. I'm deeply interested in literature, my mother tongue, English, and history. " "\n" "These subjects inspire me to explore different perspectives and understand the world around me.")
      

@bot.message_handler(func=lambda message: message.text == "Contact")
def contact_handler(message):
	bot.send_message(message.chat.id, "Tez orada qo'shiladi😁")

bot.infinity_polling()
