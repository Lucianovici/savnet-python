class Animal(object):
    class_level_field = 'Badabum!'

    def __init__(self, default_position=0):
        self.position = default_position
        self.__something_private = 'Huhuuu!'

    def move_down(self):
        print('Am mers jos')
        self.position -= 1
        return self

    def move_up(self):
        print('Am mers sus')
        self.position += 1
        return self

    @classmethod
    def modify_class_level_field(cls, value):
        cls.class_level_field = value


a = Animal(101)

a.move_up().move_down().move_up().move_up()

print(a.position)
# print(a.__something_private)  # Crashes with AttributeError

print(Animal.class_level_field)
print(a.class_level_field)

b = Animal()
b.modify_class_level_field('something_else')

# Modifying a class level variable, would affect all the other instances.
print(Animal.class_level_field)
print(a.class_level_field)
print(b.class_level_field)
