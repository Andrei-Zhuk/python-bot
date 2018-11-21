# Настройки
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import apiai, json


updater = Updater(token='709802155:AAGXZEVvNoT6FQL7JuU2SBw9L8j53UlGGG4') # Токен API к Telegram
dispatcher = updater.dispatcher
# Обработка команд
def startCommand(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Привет, давай пообщаемся?')
def textMessage(bot, update):
    request = apiai.ApiAI('05fbecb26f1349e0892e2f61f5970a52').text_request()
    request.lang = 'ru'
    request.session_id = 'The_Bobby_bot'
    request.query = update.message.text

    responseJson = json.loads(request.getresponse().read().decode('utf-8'))
    response = responseJson['result']['fulfillment']['speech']
    if response:
        bot.send_message(chat_id=update.message.chat_id, text=response)
    else:
        bot.send_message(chat_id=update.message.chat_id, text='Я Вас не совсем понял!')
# Хендлеры
start_command_handler = CommandHandler('start', startCommand)
text_message_handler = MessageHandler(Filters.text, textMessage)
# Добавляем хендлеры в диспетчер
dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)
# Начинаем поиск обновлений
updater.start_polling(clean=True)
# Останавливаем бота, если были нажаты Ctrl + C
updater.idle()