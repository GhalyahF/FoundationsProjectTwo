# UTILS AND FUNCTIONALITY
from data import stores
from components import Cart

site_name = "carted"  # Give your site a name

def welcome():
    print("Welcome to %s!\nFeel free to shop throughout the stores we have, and only checkout once!" % site_name)

def print_stores():
    """
    prints the list of stores in a nice readable format.
    """
    [print("-",store.name) for store in stores]

def get_store(store_name):
    """
    receives a name for a store, and returns the store object with that name.
    """
    store_name= pick_store()
    return store_name
    
def pick_store():
    """
    prints list of stores and prompts user to pick a store.
    """
    print_stores()
    store_name = input("Pick a store by typing its name. Or type \"checkout\" to pay your bills and say your goodbyes.\n")
    if store_name in stores:
        print("Now shopping in %s")%store.name
        get_store()
    else:
        print("No store with that name. Please try again.")
        store_name

    
def pick_products(cart, picked_store):
    """
    prints list of products and prompts user to add products to cart.
    """
    Store.print_products()

def shop():

    """
    The main shopping functionality
    """
    order= input("Add items to your cart by typing the product name exactly as it was spelled above.")
    print("Type \"back\" to go back to the main menu where you can checkout.")
    while order.lower() != "back":
            cart.append(order)
            order= input("What else would you like?")
    else:
        print_order(order_list)

def thank_you():
    print("Thank you for shopping with us at %s" % site_name)




