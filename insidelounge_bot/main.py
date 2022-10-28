#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import logging

logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)

Token ='5263530638:AAEojgbtFhp04q9U8oblNJVZ-edf4E3dQFk'
bot = telebot.TeleBot(Token)

def markup_main():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    btn_site = InlineKeyboardButton("Наш Сайт 📰"
    }, url=r"https://inside-loungebar.ru/")
    btn_photo = InlineKeyboardButton("Фотоотчет 📸", url=r"https://vk.com/albums-190888753")
    btn_specials = InlineKeyboardButton("Акции 🎁", callback_data="cb_specials")
    btn_vk = InlineKeyboardButton("Группа VK", url=r"https://vk.com/inside_loungebar")
    btn_menu = InlineKeyboardButton("Меню 🥗", url=r"https://inside-loungebar.ru/wp-content/uploads/2021/10/menu-inside-2021.pdf")
    btn_inst = InlineKeyboardButton("Instagram", url=r"https://www.instagram.com/inside_loungebar/")
    btn_book = InlineKeyboardButton("Забронировать 📌", url=r"https://512354.restoplace.ws/")
    btn_3d = InlineKeyboardButton("3D Тур 🥾", url=r"https://spb.zoon.ru/entertainment/inside_lounge_bar_na_ulitse_pravdy/")
    btn_card = InlineKeyboardButton("Добавить карту клиента 💳", callback_data="cb_card")
    markup.add(btn_site, btn_photo, btn_specials, btn_vk, btn_menu, btn_inst, btn_book, btn_3d, btn_card)

    return markup


@bot.message_handler(commands = ["start"])
def start(message):
    photos = open("meet.PNG", "rb")
    bot.send_photo(message.chat.id, photos, caption="Приветствуем вас в официальном чат-боте INSIDE 👋\n \n"
                                                    "⤵Здесь Вы можете:", reply_markup=markup_main())
@bot.message_handler(commands = ["notify"])
def start(message):
    photos = open("meet.PNG", "rb")
    bot.send_photo("-1001718561280", photos, caption="Приветствуем вас в официальном чат-боте INSIDE 👋\n \n"
                                                    "⤵Здесь Вы можете:", reply_markup=markup_main())

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "cb_menu":
        bot.send_document(call.chat.id, r"https://inside-loungebar.ru/wp-content/uploads/2021/10/menu-inside-2021.pdf")

if __name__ == '__main__':
    while 1:
        try:
            bot.polling(True)
        except Exception:
            continue

