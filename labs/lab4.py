"""
Cap4 Lab1
Exercise 1
Test the_string given password for special chars, length and more.
This is showing how functions can be used to separate concerns.

Important:
- Clean Code: Use meaningful function names that express intent. Use verbs!
- A function should typically have one responsibility. SRP - Single responsibility principle
"""


def has_valid_length(password):
    return len(password) >= 7


def has_digit(password):
    """
    Check given password for digits.
    :param password: the password string to check
    :return: True - has at least one digit, False - has no digits
    """
    for char in password:
        if char.isdigit():
            return True

    return False


def has_first_letter_uppercase(password):
    """
    Check given password for capital letter.
    :param password: the password string to check
    :return: True - when the password starts with an uppercase letter, False - otherwise
    """
    return password[0].isupper()


def has_special_chars(password):
    """
    Check given password for special characters.
    :param password: the password string to check
    :return: True - when password has at least one special character, False - when password has no special characters
    """
    special_chars = '%$!&'

    for char in password:
        for special_char in special_chars:
            if char == special_char:
                return True

    return False


def has_special_chars2(password):
    special_chars = '%$!&'

    for special_char in special_chars:
        if special_char in password:
            return True

    return False


def has_special_chars3(password):
    special_chars = '%$!&'

    for char in password:
        if char in special_chars:
            return True

    return False


def main():
    print('Checking password>')

    # Infinite loop, asking for password from input, until the password meets all requirements.
    while True:
        password = input('Give me the pass')

        condition1 = has_special_chars(password)
        if not condition1:
            print('Invalid password. No special characters')

        condition2 = has_first_letter_uppercase(password)
        if not condition2:
            print('Invalid password. No first upper case char')

        condition3 = has_valid_length(password)
        if not condition3:
            print('Invalid password. Too short password.')

        condition4 = has_digit(password)
        if not condition4:
            print('Invalid password. No digit found.')

        if condition1 and condition2 and condition3 and condition4:
            print('All good! Password is valid!')
            break


# Call the main function
main()
