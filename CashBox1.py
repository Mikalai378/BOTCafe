from CollectOrder import *


@cash_bot.message_handler(commands=['start'])
def start_cash_box(message):
    first_start(message)
    CollectOrderBot()


@cash_bot.callback_query_handler(func=lambda call: True)
def options(call):
    start(call)
    menu(call)
    back_func(call)
    minus(call)
    ok_func(call)
    delete_func(call)


@cash_bot.message_handler(content_types=['text'])
def basket_add(message):
    choice_of_art(message)
    if message.text == 'test':
        cash_bot.delete_message(message.chat.id, message.message_id)
        print(add_to_basket, money)
        total = sum(money)
        print(total)


if __name__ == '__main__':
    cash_bot.polling(none_stop=True, interval=0)
