import telebot
import requests
from telebot import types

TOKEN = "8666237647:AAH2pes9P39GDJ8SrKtSW7RQl_DQIBDNkPg"

requests.get(f"https://api.telegram.org/bot{TOKEN}/deleteWebhook")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add(types.KeyboardButton("📱 ارسال شماره", request_contact=True))
    bot.send_message(message.chat.id, "سلام! دکمه رو بزن تا شماره‌ت رو بفرستی 👇", reply_markup=markup)

@bot.message_handler(content_types=['contact'])
def contact(message):
    bot.send_message(message.chat.id, f"✅ دریافت شد!\n👤 {message.contact.first_name}\n📞 {message.contact.phone_number}")

print("bot ok")
bot.infinity_polling()
