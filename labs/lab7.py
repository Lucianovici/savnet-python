from product import Product

MAIN_MENU_ITEM_SHOW_CATEGORY = '1'
MAIN_MENU_ITEM_PRODUCT_SUBMENU = '2'
MAIN_MENU_ITEM_EXIT = '3'

PRODUCT_SUBMENU_ADD = '1'
PRODUCT_SUBMENU_LIST = '2'
PRODUCT_SUBMENU_RETURN_TO_MAIN_MENU = '3'

# TODO - Use pickle to serialize to a file.
products = []


def show_main_menu():
    print('''
    Main Menu
    1. Categories
    2. Products
    3. Exit!
    ''')


def show_categories():
    print('=' * 20)
    print('CATEGORIES')
    print('=' * 20)

    index = 1
    for category in Product.category_options:
        print(f'{index}. {category}')
        index += 1


def show_product_submenu():
    print('''
    Product Menu
    1. Add product
    2. Show products by category
    3. Return to main menu
    ''')


def get_valid_number_option(display_text, valid_options):
    number_option = None

    while number_option not in valid_options:
        number_option = input(display_text)

    return number_option


def process_main_menu():
    show_main_menu()
    return get_valid_number_option('Main menu: Choose wisely', ['1', '2', '3'])


def add_product():
    print('Add product')

    product = Product()

    while True:
        name = input('Product name')

        product.set_name(name)
        if product.validate_name():
            break
        else:
            print('Invalid name! Use letters and spaces only')

    products.append(product)

def list_products():
    print('Showing products by category')


def process_product_submenu():
    product_submenu_opt = None

    while product_submenu_opt != PRODUCT_SUBMENU_RETURN_TO_MAIN_MENU:
        product_submenu_opt = get_valid_number_option('Product submenu: Choose wisely', ['1', '2', '3'])

        if product_submenu_opt == PRODUCT_SUBMENU_ADD:
            add_product()
        elif product_submenu_opt == PRODUCT_SUBMENU_LIST:
            list_products()
        elif product_submenu_opt == PRODUCT_SUBMENU_RETURN_TO_MAIN_MENU:
            break
        else:
            print('Invalid option!')


opt = None

while opt != MAIN_MENU_ITEM_EXIT:
    opt = process_main_menu()

    if opt == MAIN_MENU_ITEM_SHOW_CATEGORY:
        show_categories()
    elif opt == MAIN_MENU_ITEM_PRODUCT_SUBMENU:
        show_product_submenu()
        process_product_submenu()
    elif opt == MAIN_MENU_ITEM_EXIT:
        break
    else:
        print('Invalid option! Try harder')
