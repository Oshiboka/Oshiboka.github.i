import telebot

# Initialize bot with your Telegram Bot Token
bot = telebot.TeleBot('6899909977:AAF4PUn1mvt2x9DWXbg03OEtLye6nT-VD10')


# Define a handler for the /start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Hello, welcome to my bot!')


# Define a handler for text messages
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


# Set up the webhook URL
webhook_url = 'https://oshiboka.github.io/'


# Set the webhook
bot.set_webhook(url=webhook_url)
# Start the bot
bot.polling()
