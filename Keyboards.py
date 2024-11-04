from telebot import types
from Server import *


def keyboard():
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Обычный заказ', callback_data='order')
    button2 = types.InlineKeyboardButton(text='Телеграм заказ', callback_data='t_order')
    markup.add(button1, button2)
    return markup


def key_menu():
    markup = types.InlineKeyboardMarkup(row_width=2)
    button1 = types.InlineKeyboardButton(text=f'{product1.name} {product1.sticker}', callback_data='product1')
    button2 = types.InlineKeyboardButton(text=f'{product2.name} {product2.sticker}', callback_data='product2')
    button3 = types.InlineKeyboardButton(text=f'{product3.name} {product3.sticker}', callback_data='product3')
    button4 = types.InlineKeyboardButton(text=f'{product4.name} {product4.sticker}', callback_data='product4')
    button5 = types.InlineKeyboardButton(text=f'{product5.name} {product5.sticker}', callback_data='product5')
    button6 = types.InlineKeyboardButton(text=f'{product6.name} {product6.sticker}', callback_data='product6')
    button7 = types.InlineKeyboardButton(text=f'{product7.name} {product7.sticker}', callback_data='product7')
    button8 = types.InlineKeyboardButton(text=f'{product8.name} {product8.sticker}', callback_data='product8')
    button9 = types.InlineKeyboardButton(text=f'{product9.name} {product9.sticker}', callback_data='product9')
    button10 = types.InlineKeyboardButton(text=f'{product10.name} {product10.sticker}', callback_data='product10')
    button11 = types.InlineKeyboardButton(text='Убрать ❌', callback_data='delete')
    button12 = types.InlineKeyboardButton(text='Оформить ✅', callback_data='send')
    button13 = types.InlineKeyboardButton(text='Назад', callback_data='back1')
    markup.add(button1, button2, button3, button4, button5, button6, button7, button8, button11, button12)
    if products < 100:
        markup.add(button13)
    return markup


def key_menu2():
    markup = types.InlineKeyboardMarkup(row_width=2)
    button1 = types.InlineKeyboardButton(text=f'{product1.name} {product1.sticker}', callback_data='product1')
    button2 = types.InlineKeyboardButton(text=f'{product2.name} {product2.sticker}', callback_data='product2')
    button3 = types.InlineKeyboardButton(text=f'{product3.name} {product3.sticker}', callback_data='product3')
    button4 = types.InlineKeyboardButton(text=f'{product4.name} {product4.sticker}', callback_data='product4')
    button5 = types.InlineKeyboardButton(text=f'{product5.name} {product5.sticker}', callback_data='product5')
    button6 = types.InlineKeyboardButton(text=f'{product6.name} {product6.sticker}', callback_data='product6')
    button7 = types.InlineKeyboardButton(text=f'{product7.name} {product7.sticker}', callback_data='product7')
    button8 = types.InlineKeyboardButton(text=f'{product8.name} {product8.sticker}', callback_data='product8')
    button9 = types.InlineKeyboardButton(text=f'{product9.name} {product9.sticker}', callback_data='product9')
    button10 = types.InlineKeyboardButton(text=f'{product10.name} {product10.sticker}', callback_data='product10')
    button11 = types.InlineKeyboardButton(text='Убрать ❌', callback_data='delete')
    button12 = types.InlineKeyboardButton(text='Оформить ✅', callback_data='send')
    button13 = types.InlineKeyboardButton(text='Отмена', callback_data='cancel')
    markup.add(button1, button2, button3, button4, button5, button6, button7, button8)
    if products < 100:
        markup.add(button11, button12)
        markup.add(button13)
    return markup


def key_art1():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    for i in range(0, len(art1)):
        if i >= 0:
            button31 = types.KeyboardButton(f'{art1[i]}')
            markup.add(button31)
        elif i >= 1:
            button32 = types.InlineKeyboardButton(f'{art1[i]}')
            markup.add(button32)
        elif i >= 2:
            button33 = types.InlineKeyboardButton(f'{art1[i]}')
            markup.add(button33)
        elif i >= 3:
            button34 = types.InlineKeyboardButton(f'{art1[i]}')
            markup.add(button34)
        elif i >= 4:
            button35 = types.InlineKeyboardButton(f'{art1[i]}')
            markup.add(button35)
        elif i >= 5:
            button36 = types.InlineKeyboardButton(f'{art1[i]}')
            markup.add(button36)
    return markup


def key_delete():
    markup = types.InlineKeyboardMarkup(row_width=1)
    for i in range(0, len(basket)):
        if i >= 0:
            button1 = types.InlineKeyboardButton(text=f'{basket[i]} ❌', callback_data='minus1')
            markup.add(button1)
        elif i >= 1:
            button2 = types.InlineKeyboardButton(text=f'{basket[i]} ❌', callback_data='minus2')
            markup.add(button2)
        elif i >= 2:
            button3 = types.InlineKeyboardButton(text=f'{basket[i]} ❌', callback_data='minus3')
            markup.add(button3)
        elif i >= 3:
            button4 = types.InlineKeyboardButton(text=f'{basket[i]} ❌', callback_data='minus4')
            markup.add(button4)
        elif i >= 4:
            button5 = types.InlineKeyboardButton(text=f'{basket[i]} ❌', callback_data='minus5')
            markup.add(button5)
        elif i >= 5:
            button6 = types.InlineKeyboardButton(text=f'{basket[i]} ❌', callback_data='minus6')
            markup.add(button6)
        elif i >= 6:
            button7 = types.InlineKeyboardButton(text=f'{basket[i]} ❌', callback_data='minus7')
            markup.add(button7)
        elif i >= 7:
            button8 = types.InlineKeyboardButton(text=f'{basket[i]} ❌', callback_data='minus8')
            markup.add(button8)
        elif i >= 8:
            button9 = types.InlineKeyboardButton(text=f'{basket[i]} ❌', callback_data='minus9')
            markup.add(button9)
        elif i >= 9:
            button10 = types.InlineKeyboardButton(text=f'{basket[i]} ❌', callback_data='minus10')
            markup.add(button10)
    button13 = types.InlineKeyboardButton(text='Отмена', callback_data='cancel2')
    markup.add(button13)
    return markup


def key_ok():
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text=f'OK',
                                         callback_data='ok')
    markup.add(button1)
    return markup


def key_collect():
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text=f'Готово', callback_data='done')
    markup.add(button1)
    return markup
