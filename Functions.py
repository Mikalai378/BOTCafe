import Server
from Keyboards import *


def first_start(message):
    cash_bot.delete_message(message.chat.id, message.message_id)
    global msg1
    msg1 = cash_bot.send_message(message.chat.id, '⭐⭐⭐⭐⭐⭐⭐Fort Cafe⭐⭐⭐⭐⭐⭐⭐', reply_markup=keyboard())


def start(call):
    if call.data == 't_order':
        cash_bot.delete_message(call.message.chat.id, call.message.message_id - 0)
        cash_bot.send_message(call.message.chat.id, 'Введите номер заказа...')
    elif call.data == 'order':
        total = sum(money)
        cash_bot.edit_message_text(chat_id=call.message.chat.id, message_id=msg1.message_id,
                                   text='⭐⭐⭐⭐⭐⭐Меню⭐⭐⭐⭐⭐⭐\n'
                                        f'Корзина: {Server.stickers_list}\n'
                                        f'Сумма: {total} руб.',
                                   reply_markup=key_menu())
    elif call.data == 'cancel':
        basket.clear()
        money.clear()
        position_quantity.clear()
        position_sticker.clear()
        Server.stickers_list = ''
        total = sum(money)
        cash_bot.edit_message_text(chat_id=call.message.chat.id, message_id=msg1.message_id,
                                   text='⭐⭐⭐⭐⭐⭐Меню⭐⭐⭐⭐⭐⭐\n'
                                        f'Корзина: {Server.stickers_list}\n'
                                        f'Сумма: {total} руб.',
                                   reply_markup=key_menu())
    elif call.data == 'cancel2':
        total = sum(money)
        cash_bot.edit_message_text(chat_id=call.message.chat.id, message_id=msg1.message_id,
                                   text='⭐⭐⭐⭐⭐⭐Меню⭐⭐⭐⭐⭐⭐\n'
                                        f'Корзина: {Server.stickers_list}\n'
                                        f'Сумма: {total} руб.',
                                   reply_markup=key_menu2())
    elif call.data == 'buy':
        order_operation(call)
        global x
        x = collect_bot.send_message(call.message.chat.id, f'{order_bill}', reply_markup=key_collect())


def back_func(call):
    if call.data == 'back1':
        Server.stickers_list = ''
        money.clear()
        basket.clear()
        cash_bot.edit_message_text(chat_id=call.message.chat.id, message_id=msg1.message_id,
                                   text='⭐⭐⭐⭐⭐⭐⭐Fort Cafe⭐⭐⭐⭐⭐⭐⭐', reply_markup=keyboard())
    elif call.data == 'back2':
        cash_bot.delete_message(call.message.chat.id, call.message.message_id - 0)
        Server.product = None


def choice_of_art(message):
    for i in range(0, len(art1)):
        if message.text == f'{art1[i]}':
            cash_bot.delete_message(message.chat.id, message.message_id - 0)
            cash_bot.delete_message(message.chat.id, message.message_id - 1)
            list_of_products[Server.product].name_art = art1[i]
            basket.append(list_of_products[Server.product].name)
            position_sticker.append(list_of_products[Server.product].sticker)
            Server.stickers_list += list_of_products[Server.product].sticker
            money.append(list_of_products[Server.product].cost * list_of_products[Server.product].quantity)
            total = sum(money)
            cash_bot.edit_message_text(chat_id=message.chat.id, message_id=msg1.message_id,
                                       text='⭐⭐⭐⭐⭐⭐Меню⭐⭐⭐⭐⭐⭐\n'
                                            f'Корзина: {Server.stickers_list}\n'
                                            f'Сумма: {total} руб.',
                                       reply_markup=key_menu2())
            print(basket[0].name_art)
            if len(basket) > 1:
                print(basket[1].name_art)


def add_to_basket(call):
    if list_of_products[Server.product].art is True:
        total = sum(money)
        cash_bot.send_message(call.message.chat.id, 'Вид:', reply_markup=key_art1())
    else:
        basket.append(list_of_products[Server.product].name)
        position_sticker.append(list_of_products[Server.product].sticker)
        Server.stickers_list += list_of_products[Server.product].sticker
        money.append(list_of_products[Server.product].cost * list_of_products[Server.product].quantity)
        total = sum(money)
        cash_bot.edit_message_text(chat_id=call.message.chat.id, message_id=msg1.message_id,
                                   text='⭐⭐⭐⭐⭐⭐Меню⭐⭐⭐⭐⭐⭐\n'
                                        f'Корзина: {Server.stickers_list}\n'
                                        f'Сумма: {total} руб.',
                                   reply_markup=key_menu2())


def menu(call):
    if call.data == 'product1':
        Server.product = 0
        cash_bot.answer_callback_query(call.id, f'{list_of_products[Server.product].sticker}')
        add_to_basket(call)
    elif call.data == 'product2':
        Server.product = 1
        cash_bot.answer_callback_query(call.id, f'{list_of_products[Server.product].sticker}')
        add_to_basket(call)
    elif call.data == 'product3':
        Server.product = 2
        cash_bot.answer_callback_query(call.id, f'{list_of_products[Server.product].sticker}')
        add_to_basket(call)
    elif call.data == 'product4':
        Server.product = 3
        cash_bot.answer_callback_query(call.id, f'{list_of_products[Server.product].sticker}')
        add_to_basket(call)
    elif call.data == 'product5':
        Server.product = 4
        cash_bot.answer_callback_query(call.id, f'{list_of_products[Server.product].sticker}')
        add_to_basket(call)
    elif call.data == 'product6':
        Server.product = 5
        cash_bot.answer_callback_query(call.id, f'{list_of_products[Server.product].sticker}')
        add_to_basket(call)
    elif call.data == 'product7':
        Server.product = 6
        cash_bot.answer_callback_query(call.id, f'{list_of_products[Server.product].sticker}')
        add_to_basket(call)
    elif call.data == 'product8':
        Server.product = 7
        cash_bot.answer_callback_query(call.id, f'{list_of_products[Server.product].sticker}')
        add_to_basket(call)
    elif call.data == 'product9':
        Server.product = 8
        cash_bot.answer_callback_query(call.id, f'{list_of_products[Server.product].sticker}')
        add_to_basket(call)
    elif call.data == 'product10':
        Server.product = 9
        cash_bot.answer_callback_query(call.id, f'{list_of_products[Server.product].sticker}')
        add_to_basket(call)


def operations(call):
    basket.append(list_of_products[Server.product].name)
    position_quantity.append(list_of_products[Server.product].quantity)
    position_sticker.append(list_of_products[Server.product].sticker)
    money.append(list_of_products[Server.product].cost * list_of_products[Server.product].quantity)


def delete_func(call):
    if call.data == 'delete':
        cash_bot.edit_message_text(chat_id=call.message.chat.id
                                   , message_id=msg1.message_id,
                                   text='⭐⭐⭐⭐⭐⭐Меню⭐⭐⭐⭐⭐⭐\n'
                                        f'Корзина: {Server.stickers_list}\n'
                                        f'Сумма: {total} руб.',
                                   reply_markup=key_delete())


def minus_help(call):
    if position_quantity[Server.product] == 0:
        del position_quantity[Server.product], money[Server.product], position_sticker[Server.product], \
            basket[Server.product]


def minus_operation(call):
    list_of_products[Server.product].quantity -= 1
    basket.remove(Server.product)
    money[Server.product] -= list_of_products[Server.product].cost
    stickers_list.replace(list_of_products[Server.product].sticker, '', 1)
    minus_help(call)
    if sum(money) == 0:
        basket.clear()
        money.clear()
        position_quantity.clear()
        position_sticker.clear()
        Server.stickers_list = ''
        cash_bot.delete_message(call.message.chat.id, call.message.message_id - 0)
    else:
        cash_bot.edit_message_text(chat_id=call.message.chat.id, message_id=msg1.message_id,
                                   text='⭐⭐⭐⭐⭐⭐Меню⭐⭐⭐⭐⭐⭐\n'
                                        f'Корзина: {Server.stickers_list}\n'
                                        f'Сумма: {total} руб.',
                                   reply_markup=key_menu2())


def minus(call):
    if call.data == 'minus1':
        Server.product = 0
        minus_operation(call)
    elif call.data == 'minus2':
        Server.product = 1
        minus_operation(call)
    elif call.data == 'minus3':
        Server.product = 2
        minus_operation(call)
    elif call.data == 'minus4':
        Server.product = 3
        minus_operation(call)
    elif call.data == 'minus5':
        Server.product = 4
        minus_operation(call)
    elif call.data == 'minus6':
        Server.product = 5
        minus_operation(call)
    elif call.data == 'minus7':
        Server.product = 6
        minus_operation(call)
    elif call.data == 'minus8':
        Server.product = 7
        minus_operation(call)
    elif call.data == 'minus9':
        Server.product = 8
        minus_operation(call)
    elif call.data == 'minus10':
        Server.product = 9
        minus_operation(call)


def ok_func(call):
    if call.data == 'ok':
        basket.clear()
        money.clear()
        position_quantity.clear()
        position_sticker.clear()
        Server.stickers_list = ''
        cash_bot.delete_message(call.message.chat.id, call.message.message_id - 0)


def order_operation(call):
    total = sum(money)
    Server.number += 1
    global order_bill
    order_bill = f'Заказ № {Server.number} 🔴\n'
    for i in range(len(basket)):
        text_bill = f'{str(position_sticker[i])} {basket[i]}  -  X{position_quantity[i]}\n'
        order_bill += text_bill
    all_orders[Server.number] = order_bill
    cash_bot.delete_message(call.message.chat.id, call.message.message_id - 0)
    cash_bot.send_message(call.message.chat.id, f'ИТОГО: {total}\n'
                                                f'{stickers_list}\n'
                                                f'Выдано клиентом:')
    print(order_bill)


def done_func(call):
    if call.data == 'done':
        order_bill = f'Заказ № {Server.number} 🟢\n'
        for i in range(len(basket)):
            text_bill = f'{str(position_sticker[i])} {basket[i]}  -  X{position_quantity[i]}\n'
            order_bill += text_bill
        collect_bot.edit_message_text(chat_id=call.message.chat.id, message_id=x.message_id, text=f'{order_bill}',
                                      reply_markup=key_collect())
