class Product(object):
    # Class level field (variable)
    category_options = {'Haine', 'Incaltaminte', 'Accesorii'}

    def __init__(self, name=None, price=None, category=None, stock=None):
        self._name = name
        self._price = price
        self.category = category
        self._stock = stock

    def input_name2(self):
        """
        Input a name for the product, until it is valid.
        This is cleaner :)
        """
        self._name = input('Product name')

        if not self.validate_name():
            self.input_name2()

        print('Nicely done. This is dope!')

    def input_name(self):
        while True:
            self._name = input('Product name')

            if self.validate_name():
                break
            else:
                print('Invalid name! Use letters and spaces only')

    def input_price(self):
        while True:
            try:
                self._price = float(input('Product price'))
                if self.validate_price():
                    break
                else:
                    print('Invalid price! Must be greater than zero.')
            except ValueError:
                print('Invalid price! Must be float number.')

    def input_stock(self):
        while True:
            try:
                self._stock = int(input('Product stock'))

                if self.validate_stock():
                    break
                else:
                    print('Invalid stock! Must be greater or equal to zero.')
            except ValueError:
                print('Invalid stock! Must be integer.')

    def input_category(self):
        while True:
            self.category = input('Product category')

            if self.validate_category():
                break
            else:
                print(f'Invalid category! Use one of these {Product.category_options}')

    def set_name(self, name):
        self._name = name

    def set_price(self, price):
        self._price = price

    def set_category(self, category):
        self.category = category

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
        """
        Validate price: Must be `float` and greater than zero.
        :return: True when valid, False invalid.
        """
        if type(self._price) is not float:
            return False

        if self._price <= 0.0:
            return False

        return True

    def validate_category(self):
        if self.category not in Product.category_options:
            return False

        return True

    def validate_stock(self):
        if type(self._stock) is not int:
            return False

        if self._stock < 0:
            return False

        return True

    def __str__(self):
        return f'Product {self._name}, ${self._price}, stock: {self._stock}'

    def get_str_the_zoli_way(self):
        return f'Category: {self.category} || Product {self._name}, ${self._price}, stock: {self._stock}'

    def display_product_as_per_specs(self):
        print(f'Name: {self._name}')
        print(f'Price: {self._price}')
        print(f'Stock: {self._stock}')
        print('-' * 15)
