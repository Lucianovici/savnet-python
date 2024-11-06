class Product(object):
    # Class level field (variable)
    category_options = {'Haine', 'Incaltaminte', 'Accesorii'}

    def __init__(self, name=None, price=None, category=None, stock=None):
        self._name = name
        self._price = price
        self._category = category
        self._stock = stock

    def set_name(self, name):
        self._name = name

    def set_price(self, price):
        self._price = price

    def set_category(self, category):
        self._category = category

    def set_stock(self, stock):
        self._stock = stock

    def validate_name(self):
        """
        Validate name: Just letters and spaces!
        :return True when valid, False invalid.
        """
        for char in self._name:
            if not (char.isalpha() or char.isspace()):
                return False
            
        return True

    def validate_price(self):
        # Pseudocode validate structure
        # Validate price type - if is invalid - return False
        # Validate price value - if is invalid - return False
        # If all good, in the end - return True
        raise NotImplementedError

    def validate_category(self):
        raise NotImplementedError

    def validate_stock(self):
        raise NotImplementedError

    def display(self):
        print(f'Product {self._name}, ${self._price}, stock: {self._stock}')
