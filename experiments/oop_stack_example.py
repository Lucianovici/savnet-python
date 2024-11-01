class Stack(object):
    def __init__(self, default_list):
        self.__stack_list = default_list or []

    def push(self, value):
        self.__stack_list.append(value)

    def pop(self):
        value = self.__stack_list[-1]
        del self.__stack_list[-1]
        return value

    def display_stack(self):
        print(self.__stack_list)

    def is_empty(self):
        """
        Test if the stack is empty or not.
        :return: True when empty, False otherwise
        """
        return len(self.__stack_list) == 0


# Let's move all items from s1 stack to s2 stack.
s1 = Stack([item for item in range(10)])
s2 = Stack([])

while not s1.is_empty():
    s2.push(s1.pop())

    print('s1:')
    s1.display_stack()
    print('s2:')
    s2.display_stack()

print('Tank you! WAR? Declare variables NOT WAR.')
