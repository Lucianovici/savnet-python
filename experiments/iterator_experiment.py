class Iterator:
    def __init__(self, length):
        print('__init__ called: Initiate the instance')
        self._length = length
        self.__current = 0

    def __iter__(self):
        print('__iter__ called: Initiate the iterable')
        self.__current = 0
        return self

    def __next__(self):
        print('__next__ called: Go to next element')
        self.__current += 1

        if self.__current > self._length:
            raise StopIteration

        return self.__current ** 2


iter_instance = Iterator(11)

for i in iter_instance:
    print(i)
