class Mama(object):
    soft_skills = ['ALL']


class Tata(object):
    hard_skills = ['sapa']


class Kid(Mama, Tata):
    pass


child = Kid()
print(child.hard_skills)
print(child.soft_skills)


class Animal(object):

    def __init__(self, legs):
        self._legs = legs

    def set_number_of_legs(self, legs):
        self._legs = legs


class Mammal(Animal):

    def __init__(self, legs, babies):
        super().__init__(legs)
        self._number_of_born_babies = babies

    def set_number_of_born_babies(self, babies):
        self._number_of_born_babies = babies


class Dog(Mammal):

    def __init__(self, legs, babies, breed):
        super().__init__(legs, babies)
        self._breed = breed

    def say_hi(self):
        print(f'I am a {self._breed}, I have {self._number_of_born_babies} babies, and I have {self._legs} legs')


tasha = Dog(4, 2, 'Tomberonez')
tasha.say_hi()

print(type(tasha))
