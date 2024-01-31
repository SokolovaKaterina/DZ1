import random

import telebot

from funcs.datatime import gel_welcome
from funcs.functionality import functionality
from init_bot import bot


@bot.message_handler(commands=["start", "help"])
def start(message: telebot.types.Message):
    text = f"{gel_welcome()} \n" \
           f"Я бот для выбора фильма для вашего вечера🎬\n\n" \
           f"Вот что я имею:\n" \
           f"{functionality()}"
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=["get_film_random"])
def get_film_random(message: telebot.types.Message):
    with open("get_film_random.txt", "r", encoding="UTF-8") as file:
        film = file.read().split("\n")
    films = random.choice(film)
    bot.send_message(message.chat.id, f"Сегодня вечером стоит посмотреть фильм '{films}'", parse_mode="markdown")


@bot.message_handler(commands=["get_film_genre"])
def det_film_genre(message: telebot.types.Message):
    markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=2)
    markup.add(
        telebot.types.KeyboardButton("Боевик"),
        telebot.types.KeyboardButton("Драма"),
        telebot.types.KeyboardButton("Комедия"),
        telebot.types.KeyboardButton("Ужасы"),
        telebot.types.KeyboardButton("Мультфильм")
    )
    bot.reply_to(message, "Какой жанр вам нравится?", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "Боевик")
def handle_action(message: telebot.types.Message):
    markup = telebot.util.quick_markup({
        "Бесславные ублюдки": {"url": "https://www.kinopoisk.ru/film/9691/"},
        "Дэдпул": {"url": "https://www.kinopoisk.ru/film/462360/"}
    })
    bot.reply_to(message, "Вот пара фильмов в жанре 'Боевик':", reply_markup=markup)
    bot.send_message(message.chat.id, f"Выберете следующий шаг:\n{functionality()}")
    bot.clear_reply_handlers_by_message_id(message.chat.id, message.message_id)


@bot.message_handler(func=lambda message: message.text == "Драма")
def handle_action(message: telebot.types.Message):
    markup = telebot.util.quick_markup({
        "1+1": {"url": "https://www.kinopoisk.ru/film/535341/"},
        "Джокер": {"url": "https://www.kinopoisk.ru/film/1048334/"}
    })
    bot.reply_to(message, "Вот пара фильмов в жанре 'Драма':", reply_markup=markup)
    bot.send_message(message.chat.id, f"Выберете следующий шаг:\n{functionality()}")


@bot.message_handler(func=lambda message: message.text == "Комедия")
def handle_action(message: telebot.types.Message):
    markup = telebot.util.quick_markup({
        "Холоп": {"url": "https://www.kinopoisk.ru/film/1183582/"},
        "Один дома": {"url": "https://www.kinopoisk.ru/film/8124/"}
    })
    bot.reply_to(message, "Вот пара фильмов в жанре 'Комедия':", reply_markup=markup)
    bot.send_message(message.chat.id, f"Выберете следующий шаг:\n{functionality()}")


@bot.message_handler(func=lambda message: message.text == "Ужасы")
def handle_action(message: telebot.types.Message):
    markup = telebot.util.quick_markup({
        "Чужой": {"url": "https://www.kinopoisk.ru/film/386/"},
        "Заклятие": {"url": "https://www.kinopoisk.ru/film/468994/"}
    })
    bot.reply_to(message, "Вот пара фильмов в жанре 'Ужасы':", reply_markup=markup)
    bot.send_message(message.chat.id, f"Выберете следующий шаг:\n{functionality()}")


@bot.message_handler(func=lambda message: message.text == "Мультфильм")
def handle_action(message: telebot.types.Message):
    markup = telebot.util.quick_markup({
        "Корпорация монстров": {"url": "https://www.kinopoisk.ru/film/458/"},
        "Три богатыря и Конь на троне": {"url": "https://www.kinopoisk.ru/film/4419497/"}
    })
    bot.reply_to(message, "Вот пара фильмов в жанре 'Мультфильм':", reply_markup=markup)
    bot.send_message(message.chat.id, f"Выберете следующий шаг:\n{functionality()}")


@bot.message_handler(commands=["my_favorite"])
def get_film_random(message: telebot.types.Message):
    text = "[Век Адалин](https://www.kinopoisk.ru/film/522876/)"
    bot.send_message(message.chat.id, f"Мой самый любимый фильм это '{text}'", parse_mode="markdown")
    bot.send_message(message.chat.id, f"Выберете следующий шаг:\n{functionality()}")


@bot.message_handler(commands=["end"])
def end(message: telebot.types.Message):
    markup = telebot.types.ReplyKeyboardRemove()
    text = f"Спасибо! Пока)"
    bot.send_message(message.chat.id, text, reply_markup=markup)

