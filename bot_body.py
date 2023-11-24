import telebot
#from aiogram import Bot, Dispatcher, types
#from aiogram.types.web_app_info import WebAppInfo
from docx import Document
from telebot import types
import webbrowser
import json
import pandas as pd
from docx import Document
from docx.shared import Inches

bot = telebot.TeleBot('5861648013:AAG0ICuPqc7Zf8KEdgvh1NAVQ0zybw28LSc')

with open('abbreviaturka.json', 'r') as file:
    abbreviations = json.load(file)


@bot.message_handler(commands=['start'])  # декоратор, который обрабатывает команды и выдает какой-либо заданный ответ
def main(message):
    bot.send_message(message.chat.id,
                             f'Привет, {message.from_user.first_name}! Я могу помочь тебе с расшифровкой аббревиатур.')


@bot.message_handler(commands=['help'])
def main(message: types.Message):
    bot.send_message(message.chat.id,
                             'Я могу помочь тебе расшифровать аббревиатуру. Если я ее не знаю, то скоро выучу или ты можешь сам пополнить мой словарь!')


@bot.message_handler(func=lambda message: True)
def echo(message):
    text = message.text.lower()  # Приводим введенный текст к нижнему регистру

    found = False
    for abbreviation, decryption in abbreviations.items():
        if text.lower() == abbreviation.lower():  # Сравниваем введенный текст и аббревиатуру в нижнем регистре
            bot.send_message(message.chat.id, decryption)
            found = True
            break

    if not found:
        bot.send_message(message.chat.id, 'К сожалению, я не знаю расшифровки этой аббревиатуры.')


bot.polling(none_stop=True)


# обновление списка аббревиатур(на доработке)

#@bot.message_handler(commands=['update'])
#def update_abbreviations(message):
 #   text = message.text.split(maxsplit=1)[1]
  #  try:
   #     new_abbreviations = json.loads(text)
    #    abbreviations.update(new_abbreviations)
     #   bot.send_message(message.chat.id, 'Словарь обновлен!')
    #except:
     #   bot.send_message(message.chat.id, 'Не удалось обновить словарь.')
