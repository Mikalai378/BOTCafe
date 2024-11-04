class Menu:
    def __init__(self, name, cost, sticker, quantity):
        self.name = name
        self.cost = cost
        self.sticker = sticker
        self.quantity = quantity


product1 = Menu('Чай', 1.00, '🫖', 0)
product2 = Menu('Кофе', 1.00, '☕️', 0)
product3 = Menu('Мохито', 1.00, '🍹', 0)
product4 = Menu('Кола', 1.00, '🥤', 0)
product5 = Menu('Пицца', 1.00, '🍕', 0)
product6 = Menu('Сэндвич', 1.00, '🥪', 0)
product7 = Menu('Круасан', 1.00, '🥐', 0)
product8 = Menu('Мороженое', 1.00, '🍦', 0)
product9 = Menu(None, None, None, None)
product10 = Menu(None, None, None, None)

list_of_products = [product1, product2, product3, product4, product5, product6, product7, product8, product9, product10]
all_orders = {}
products = 8
product = None
basket = []
money = []
position_quantity = []
position_sticker = []
stickers_list = ''
number = 0
total = sum(money)
wait1 = True
wait2 = True