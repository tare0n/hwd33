class Item:
    @classmethod
    def __check(cls, name, price, quantity):
        if not isinstance(name, str):
            raise TypeError("name should be string")
        if not (isinstance(price, int) or isinstance(price, float)):
            raise TypeError("price should be number")
        if not isinstance(quantity, int):
            raise TypeError("quantity should be int")

    def __init__(self, name, price, quantity=0):
        self.__check(name, price, quantity)

        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"Item({self.name}, {self.price}, {self.quantity})"


class Phone(Item):
    def __init__(self, name, price, quantity, broken_phones):
        if not isinstance(broken_phones, int):
            raise TypeError("number of broken phones should be int")
        super().__init__(name, price, quantity)
        self.broken_phones = broken_phones

    def __str__(self):
        return f"Phone(name: {self.name}, price: {self.price}, " \
               f"quantity: {self.quantity}, number of broken phones: {self.broken_phones})"

