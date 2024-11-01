import random


class Animal(object):
    class_level_field = 'ANIMAL'  # class level variable / field

    def __init__(self, age):
        """Constructor. it is called automatically when class is instantiated"""
        self._name = None  # this is an instance variable / field.
        self._age = age
        self._legs_number = None
        self.__soul_number = random.randint(0, 100)  # private field

    def __del__(self):
        """Destructor: Kind of like a testament - Last will, before destroying the object"""
        print(f'Bye bye {self._name}')

    def set_name(self, name):
        self._name = name

    def set_number_of_legs(self, legs_number):
        self._legs_number = legs_number

    def say_hi(self):
        print(f'Hi! My age is {self._age}.')

        if self._name is not None:
            print(f'Hi my name is: {self._name}')
        if self._legs_number is not None:
            print(f'I have {self._legs_number} legs')

    def confess_yourself(self):
        if self.__soul_number > 50:
            print('I am high state being')
        else:
            print('I don\'t like you!')


def main():
    print(Animal.class_level_field)

    # instantiate an Animal
    tasha = Animal(6)
    tasha.set_name('Tasha')
    tasha.confess_yourself()

    print(tasha.class_level_field)

    # instantiate another Animal
    thor = Animal(1)
    thor.set_name('Thor')
    thor.set_number_of_legs(4)
    thor.confess_yourself()

    # Destroy Thor! - this is usually not necessary, because at the end of the block is
    del thor

    print('Bla bla!')

    thor.say_hi()  # Will raise UnboundLocalError, because thor is destroyed already.
    tasha.say_hi()

    # print(tasha.__soul_number)  # will break, can't access private method.


main()
