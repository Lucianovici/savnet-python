import pickle
import random
from collections import defaultdict

from product import Product

MAIN_MENU_ITEM_SHOW_CATEGORY = '1'
MAIN_MENU_ITEM_PRODUCT_SUBMENU = '2'
MAIN_MENU_ITEM_EXIT = '3'

MAIN_MENU_ITEMS = [MAIN_MENU_ITEM_SHOW_CATEGORY, MAIN_MENU_ITEM_PRODUCT_SUBMENU, MAIN_MENU_ITEM_EXIT]

PRODUCT_SUBMENU_ADD = '1'
PRODUCT_SUBMENU_LIST = '2'
PRODUCT_SUBMENU_LOAD_FROM_FILE = '3'
PRODUCT_SUBMENU_GENERATE_RANDOM = '4'
PRODUCT_SUBMENU_SAVE_TO_FILE = '5'
PRODUCT_SUBMENU_RETURN_TO_MAIN_MENU = '6'
PRODUCT_SUBMENU_ITEMS = [
    PRODUCT_SUBMENU_ADD, PRODUCT_SUBMENU_LIST, PRODUCT_SUBMENU_LOAD_FROM_FILE, PRODUCT_SUBMENU_GENERATE_RANDOM,
    PRODUCT_SUBMENU_SAVE_TO_FILE, PRODUCT_SUBMENU_RETURN_TO_MAIN_MENU
]

# TODO 1. Show list of products by category | Done.
# TODO 2. Use pickle to serialize to a file. | Done.
# TODO 3. Recursive function/method call vs while for input get data from keyboard | Done.
# TODO 4. Improvement: Press any key to continue | Done.

random_name_options = ['Fusta', 'Hanorac', 'Geacă', 'Tricou']
random_color_options = ['Red', 'Green', 'Blue']

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

    input_whatever()


def show_product_submenu():
    print('''
    Product Menu
    1. Add product
    2. Show products by category
    3. Load products from file
    4. Generate random products
    5. Save products to file
    6. Return to main menu
    ''')


def get_valid_number_option(display_text, valid_options):
    number_option = None

    while number_option not in valid_options:
        number_option = input(display_text)
        if number_option not in valid_options:
            print('Invalid option!')

    return number_option


def process_main_menu():
    show_main_menu()

    return get_valid_number_option('Main menu: Choose wisely', MAIN_MENU_ITEMS)


def add_product():
    print('Add product ...')

    product = Product()

    product.input_category()
    product.input_name()
    product.input_price()
    product.input_stock()

    products.append(product)
    print(f'Product {product} added successfully')


def list_products_old_school():
    """
    List products by category.
    """
    for category_key in Product.category_options:
        print(category_key)
        for product in products:
            if category_key == product.category:
                print(product)


def list_products_old_school_with_dict():
    """
    List products by category.
    """
    product_dict = defaultdict(list)

    for product in products:
        product_dict[product.category].append(product)

    for category_key, product_list_from_category in product_dict.items():
        print(category_key)
        for product in product_list_from_category:
            print(product)


def list_products_the_specs_way():
    for category_key in Product.category_options:
        print('=' * 15)
        print(category_key)
        print('=' * 15)

        for product in [p for p in products if p.category == category_key]:
            product.display_product_as_per_specs()

    input_whatever()


def input_whatever():
    _ = input('\n\nPress `enter` to continue ...')


def list_products_the_zoli_way():
    sorted_list_of_products_by_category = sorted(products, key=lambda c: c.category)

    for p in sorted_list_of_products_by_category:
        print(p.get_str_the_zoli_way())


def load_products_from_file():
    global products  # this is not usually acceptable, but we need to use the global products here.

    with open('products.pkl', 'rb') as file:
        products = pickle.load(file)

    print(f'Loaded {len(products)} products from file!')


def save_products_to_file():
    with open('products.pkl', 'wb') as file:
        pickle.dump(products, file)

    print(f'Saved {len(products)} products to file!')


def generate_random_products():
    global products

    products = [
        Product(
            category=random.choice(list(Product.category_options)),
            name=f'{random.choice(random_name_options)} {random.choice(random_color_options)}',
            price=float(random.randint(1000, 1000000) / 100),
            stock=random.randint(0, 30) * index
        )
        for index in range(10)
    ]

    print(f'Generated {len(products)} products for you sir/madam/others lgbtQ++')


def process_product_submenu():
    product_submenu_opt = None

    while product_submenu_opt != PRODUCT_SUBMENU_RETURN_TO_MAIN_MENU:
        show_product_submenu()
        product_submenu_opt = get_valid_number_option('Product submenu: Choose wisely', PRODUCT_SUBMENU_ITEMS)

        if product_submenu_opt == PRODUCT_SUBMENU_ADD:
            add_product()
        elif product_submenu_opt == PRODUCT_SUBMENU_LIST:
            # list_products_old_school()
            # list_products_old_school_with_dict()
            # list_products_the_zoli_way()
            list_products_the_specs_way()
        elif product_submenu_opt == PRODUCT_SUBMENU_LOAD_FROM_FILE:
            load_products_from_file()
        elif product_submenu_opt == PRODUCT_SUBMENU_GENERATE_RANDOM:
            generate_random_products()
        elif product_submenu_opt == PRODUCT_SUBMENU_SAVE_TO_FILE:
            save_products_to_file()
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
        process_product_submenu()
    elif opt == MAIN_MENU_ITEM_EXIT:
        break
    else:
        print('Invalid option! Try harder')
