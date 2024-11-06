class Animal(object):

    def __init__(self):
        self.position = 0
        self.__something_private = 'Huhuuu!'

    def move_down(self):
        print('Am mers jos')
        self.position -= 1
        return self

    def move_up(self):
        print('Am mers sus')
        self.position += 1
        return self


a = Animal()

a.move_up().move_down().move_up().move_up()

print(a.position)
print(a.__something_private)  # Crashes with AttributeError
