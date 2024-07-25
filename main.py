import telebot
from config import keys, Token
from extensions import CryptoConvert, APIException


bot = telebot.TeleBot(Token)



@bot.message_handler(commands=['start','help',])
def help(message: telebot.types.Message):
    text = ('''Чтобы начать работу введите команду боту в следующем формате: \n<имя валюты>\<в какую валюту превести>\<количество переводимой валюты>.\nЧтобы посмотреть список валют введите команду /values
            ''')
    bot.reply_to(message,text)


@bot.message_handler(commands=['values',])
def values(message:telebot.types.Message):
    text = 'Доступные валюты:'
    for i in keys:
        text = '\n'.join((text,i,))
    bot.reply_to(message,text)


@bot.message_handler(content_types=['text',])
def convert(message:telebot.types.Message):
    try:
        values = message.text.split()
        if len(values) != 3:
            raise APIException('Должно быть 2 слова и 1 число!')
        quote, base, amount = values
        total_sum = CryptoConvert.get_price(quote, base, amount)
    except APIException as e:
        bot.reply_to(message,f'Ошибка в введенных данных. {e}')
    except Exception as e:
        bot.reply_to(message,f'Ошибка на сервере. {}')
    else:
        # quote, base, amount = values
        # total_sum = CryptoConvert.convert(quote, base, amount)
        bot.send_message(message.chat.id,f'Цена {amount} {quote} в {base} - {total_sum}')


bot.polling()

