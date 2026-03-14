import telebot
import os

TOKEN = os.getenv("7033025370:AAG-OORaOqxTzPC6JQq3FUhqngxnqMI-b20")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Bot is running on Railway!")

print("Bot Started")
bot.infinity_polling()
