import telebot
import requests
from telebot import types

API_TOKEN = '5760865237:AAFfobB_JX6o9_64F8KGrWTlZe3DM75PcR8'


class SportBot(telebot.TeleBot):
    def __init__(self, token):
        super().__init__(token)
        self.state = {}


bot = SportBot(API_TOKEN)


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.state[message.chat.id] = 'wait'
    print(bot.state)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Вк")
    item3 = types.KeyboardButton("матчи")
    markup.add(item1)
    markup.add(item3)
    bot.send_message(message.chat.id, "ЧТО ТЕБЕ НУЖНО?",  reply_markup=markup)


@bot.message_handler(func=lambda message: bot.state[message.chat.id] == 'matches')
def get_home_score(message):
    url = "https://football-prediction-api.p.rapidapi.com/api/v2/predictions"
    querystring = {"market": "classic", "iso_date": "2021-11-24", "federation": "UEFA"}
    headers = {
        "X-RapidAPI-Key": "6c6399ba28mshfc680ae737cc175p139fbajsn00b1697f3488",
        "X-RapidAPI-Host": "football-prediction-api.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    for i in response.json()["data"]:
        if i['home_team'] == message.text:
            bot.send_message(message.chat.id, i["result"])
            break
    print(response.json()["data"])
    bot.state[message.chat.id] = 'wait'


@bot.message_handler(func=lambda message: bot.state[message.chat.id] == 'wait')
def get_choice(message):
    if message.text == "Вк":
        bot.state[message.chat.id] = 'vk'
        bot.send_message(message.chat.id, "https://vk.com/sasha_belov2007")
    if message.text == "матчи":
        bot.state[message.chat.id] = 'matches'
        bot.send_message(message.chat.id, "введите название команды")


bot.infinity_polling()