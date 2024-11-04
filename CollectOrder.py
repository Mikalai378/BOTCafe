from Functions import *


def CollectOrderBot():
    @collect_bot.message_handler(commands=['start'])
    def start_collect(message):
        collect_bot.delete_message(message.chat.id, message.message_id)
        collect_bot.send_message(message.chat.id, '⭐⭐⭐⭐⭐⭐⭐Fort Cafe Collect Order⭐⭐⭐⭐⭐⭐⭐')

    @collect_bot.callback_query_handler(func=lambda call: True)
    def operations_collect(call):
        done_func(call)
        start(call)

    collect_bot.polling(none_stop=True, interval=0)
