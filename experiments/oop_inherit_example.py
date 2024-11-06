class Animal(object):
    """Base class. Animal"""

    def __init__(self, name, age):
        self._name = name
        self._age = age
        self._position = 0

    def say_hi(self):
        print(f'{self._name} I want to say Hi! to the world.')

    def display_position(self):
        print(f'Position is {self._position}')

    def walk_up(self):
        self._position += 1

    def walk_down(self):
        self._position -= 1


class Caine(Animal):

    def __init__(self, name, age, breed):
        """
        This extends the __init__ (constructor) from base/parent class (Animal)
        Extends = The behaviour of the method from the base class + the behaviour wanted here.
        """
        # Animal.__init__(self, name, age)  # Not recommended way to call super (my opinion)
        super().__init__(name, age)
        self._breed = breed

    def say_hi(self):
        """
        This replaces the say_hi from the base/parent class (Animal)
        """
        print(f'{self._name} I want to say Hi! to the world. I am {self._breed}')

    def walk_up(self, steps=1):
        """
        This replaces the behaviour of walk_up method from the base class (Animal).
        It is doing so, by using the super method i.e. Animal.walk_up
        """
        for step in range(steps):
            super(Caine, self).walk_up()

    def bark(self):
        # print('Bark Bark!', self._name)
        # print(f'Bark Bark! {self._name}')
        print('Bark Bark! {the_name}'.format(the_name=self._name))


simple_animal = Animal('Delfin', 11)
simple_animal.say_hi()
simple_animal.walk_up()
simple_animal.walk_up()
simple_animal.display_position()

catzel = Caine('Tasha', 10, 'Tomberonez')
catzel.say_hi()
catzel.bark()

catzel.walk_up(4)
catzel.display_position()
catzel.walk_up()
catzel.display_position()
