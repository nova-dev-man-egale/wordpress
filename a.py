import telebot
bot = telebot.TeleBot("439179526:AAHQtWwyBvNmA7umNBFy8iMclj8HyNRRe5w")
@bot.message_handler(commands=['send'])
def send(m):
    bot.send_document(m.chat.id,open("nova.apk"))
    
bot.polling(True)
