import telebot
from telebot import StateMemoryStorage

from config import API_TOKEN

bot = telebot.TeleBot(API_TOKEN, state_storage=StateMemoryStorage())
