class Store:
    def __init__(self, name):
        self.name = name
        self.products = []
    def add_product(self, new_product):
        self.products.append(new_product)
        return self
    def sell_product(self,id):
        del self.products[id]
        return self
    def inflation(self, percent_increase):
        for i in range(len(self.products)):
            self.products[i] = self.products[i].update_price(percent_increase,True)
        return self
    def set_clearance(self,category,percent_discount):
        for i in range(len(self.products)):
            if self.products[i].category == category:
                self.products[i] = self.products[i].update_price(percent_discount)
        return self

class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
    def update_price(self, percent_change, is_increased=False):
        if is_increased:
            self.price += self.price*percent_change
            self.price = round(self.price,2)
        else:
            self.price -= self.price*percent_change
            self.price = round(self.price,2)
        return self
    def print_info(self):
        print(f"product name: {self.name}")
        print(f"product price: {self.price}")
        print(f"product category: {self.category}")
        return self

heb = Store("heb")
heb.add_product(Product("tomato",.20,"produce")).add_product(Product("cucumber", .40, "produce")).add_product(Product("chicken",5,"meat")).sell_product(0).set_clearance("meat",.50).inflation(.02)
