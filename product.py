class Product:
    def __init__(self, name, price, category, id):
        self.name = name
        self.price = price
        self.category = category
        self.id = id

    def update_price(self, percent_change, is_increased):
        if is_increased == True:
            self.price = self.price * (percent_change / 100 + 1)
        else:
            self.price = self.price * (1 - percent_change / 100)
        return self

    def print_info(self):
        print(self.name, self.price, self.category, self.id)