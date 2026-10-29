from catalog import store_items # import catalog


# Global variable - list
cart = []


# Store name and menu

def header(text):
    print("----------------")
    print(text)
    print("----------------")


def menu():
    print("Menu")
    print(" 1.- View Catalog")
    print(" 2.- Search Product")
    print(" 3.- View Cart")

    # Add more features

    print(" Q.- Quit")


# Catalog and Cart Functions

def print_catalog():
    header("- Our Catalog -")

    for prod in store_items:
        print(f'| {prod["id"]} | {prod["title"].ljust(15)} | ${prod["price"]:.2f}')

    answer = input("Type ID to add (N to close): ")

    if answer.lower() == "n":
        return
    else:
        add_product_to_cart(answer)


def add_product_to_cart(prod_id):
    found = False

    for prod in store_items:

        if str(prod["id"]) == str(prod_id):
            found = True

            cart.append(prod)

            print(f'{prod["title"]} added to your cart.')

            break

    if not found:
        print("**ERROR: Invalid ID")


def search_product():

    text = input("Search text: ").lower()

    found = False

    for prod in store_items:

        if text in prod["title"].lower():

            found = True

            print(f'Found: ID {prod["id"]} | {prod["title"]} | ${prod["price"]}')

            choice = input("Do you want to add this item to your cart? (y/n): ")

            if choice.lower() == "y":
                add_product_to_cart(prod["id"])

            break # stop after first match

    if not found:
        print("Sorry, this item doesn't exist.")


def view_cart():

    header("Your Cart")

    if not cart:
        print("your cart is empty")

    else:

        for prod in cart:
            print(f'Found: ID {prod["id"]} | {prod["title"]} | ${prod["price"]}')



""" 
MINI CHALLENGE: 

    1. print header "your cart"
    2. if check if cart is empty
    3. else return all items in cart

"""


# Complete mini challenge here:
def view_cart():
    # call your header function here

# MAIN PROGRAM LOOP

options = ""

while options != "q" and options != "Q":

    header("Welcome to Store x")

    menu()

    options = input("Choose an option: ")

    if options == "1":
        print_catalog()

    elif options == "2":
        search_product()

    elif options == "3":
        print("View cart")

    elif options == "q" or options == "Q":

        print("Good Bye!")

        break

    else:

        print("**ERROR: Invalid Option, select from menu")





    