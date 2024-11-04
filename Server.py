import telebot


cash_bot = telebot.TeleBot('') #введите токен
collect_bot = telebot.TeleBot('') #введите токен


class Menu:
    def __init__(self, name, art, name_art, cost, sticker, quantity):
        self.name = name
        self.art = art
        self.name_art = name_art
        self.cost = cost
        self.sticker = sticker
        self.quantity = quantity


product1 = Menu('Чай', False, '', 1.00, '🫖', 1)
product2 = Menu('Кофе', False, '',  1.00, '☕️', 1)
product3 = Menu('Мохито', True, '',  1.00, '🍹', 1)
product4 = Menu('Кола', False, '',  1.00, '🥤', 1)
product5 = Menu('Пицца', False, '',  1.00, '🍕', 1)
product6 = Menu('Сэндвич', False, '',  1.00, '🥪', 1)
product7 = Menu('Круасан', False, '',  1.00, '🥐', 1)
product8 = Menu('Мороженое', False, '',  1.00, '🍦', 1)
product9 = Menu(None, False,  None, None, None, 0)
product10 = Menu(None, False,  None, None, None, 0)

list_of_products = [product1, product2, product3, product4, product5, product6, product7, product8, product9, product10]
all_orders = {}
products = 8
product = None
basket = []
money = []
art1 = ['Классический', 'Арбузный', 'Лимонный', 'Малиновый']
position_quantity = []
position_sticker = []
stickers_list = ''
number = 0
total = sum(money)
wait1 = True
wait2 = True
in_proces = [1, 2, 3]
orders_done = []
