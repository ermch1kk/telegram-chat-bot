import telebot

bot = telebot.TeleBot('your token') # token we take in botfather
# also u can move token to .env file


@bot.message_handler(commands=['start']) # this decorator only processes commands
def start_message(message):
    bot.send_message(message.chat.id, 'Hey, u pressed /start. Lets go!')

@bot.message_handler(content_types=['text']) # this decorator can handle diffrent messages, in [] we put a type of message
def send_text(message):
    # now we can type diffrent messages
    # for example : 
    if message.text.lower() == 'Hi':
        bot.send_message(message.chat.id, 'Hello, my dear friend!') 

    # if u wanna to say 'bye', u need :
    if message.text.lower() == 'bye':
        bot.send_message(message.chat.id, 'See u next time, bye!') 
