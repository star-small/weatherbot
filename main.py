import telebot
from sunnyside import Sunnyside
import math

ref = Sunnyside("5d06ad237e3e6019b2d12b3638b5ccd5", "celsius")
api = ref.current_weather()
bot = telebot.TeleBot('1443177814:AAEe9Wa5hDp-RYTzUBnKLmHJqX007QsnLWk')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Напишите название города, чтобы узнать подробную информацию о нём')


@bot.message_handler(content_types=['text'])
def weather(message):
    try:
        city = message.text
        response = api.get_current_weather_by_city_name('{}'.format(city))
        temp = str(round(response['main']['temp'] - 273, 2))
        feel = str(round(response['main']['feels_like'] - 273, 2))
        wind = str(response['wind']['speed']) + 'м/с'

        bot.send_message(message.chat.id, 'Погода в городе {}: '.format(city) + temp + '\nЧувствуется как: {}'.format(feel) + '\nСкорость ветра: {}'.format(wind))
    except:
        bot.send_message(message.chat.id, 'Некорректно введённый формат')


bot.polling()
