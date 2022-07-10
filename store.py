class Store:
    product_list = []
    def __init__(self, name):
        self.name = name
    
    def print_product_list(self):
        for x in self.product_list:
            x.print_info()

    def add_product(self, new_product):
        self.product_list.append(new_product)
        return self

    def sell_product(self, id_num):
        for x in self.product_list:
            if x.id == id_num:
                index = self.product_list.index(x)
                self.product_list.pop(index)
        return self
    
    def inflation(self,percent_increase):
        for x in self.product_list:
            x.update_price(percent_increase, True)
        return self

    def set_clearance(self, category, percent_discount):
        for x in self.product_list:
            if x.category == category:
                x.update_price(percent_discount, False)
        return self