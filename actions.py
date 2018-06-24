
# UTILS AND FUNCTIONALITY
from data import stores
from components import Cart

site_name = "www.carted.com"  # Give your site a name


def welcome():
    print("Welcome to %s!\nFeel free to shop throughout the stores we have, and only checkout once!" % site_name)
    pick_store()

def print_stores():
    """
    prints the list of stores in a nice readable format.
    """
    [print("-",store.name) for store in stores]

def get_store(store_name):
    """
    receives a name for a store, and returns the store object with that name.
    """
    for store in stores:
        if store.name.lower() == store_name.lower():
            return store.name
        else:
            return False
            
    
def pick_store():
    
    """
    prints list of stores and prompts user to pick a store.
    """
    print_stores()
    store_name= input("Pick a store by typing its name. Or type \"checkout\" to pay your bills and say your goodbyes.\n")
    if store_name.lower() != "checkout":
        return "checkout"
    else:
        picked_store= get_store(store_name)
        return picked_store

    
    
def pick_products(cart,picked_store):
    """
    prints list of products and prompts user to add products to cart.
    """
    print()
    print("Add items to your cart by typing the product name exactly as it was spelled above.")
    print("Type \"back\" to go back to the main menu where you can checkout.")
    user_input= input()
    if user_input != "back" and user_input.lower() in stores:
        for store in picked_store:
            picked_store.print_products
 
      
            

def shop():

    """
    The main shopping functionality
    """
    user_input= ""
    while user_input.lower() != "checkout":
        picked_store= pick_store()
        if picked_store == "checkout":
            break
        picked_store.print_products
        print("Add items to your cart by typing them exactly as spelled above.")
        print("Type \"back\" to return to the main menu where you can checkout.")
        #user_input= pick_products(cart,picked_store)
    

 
  
            

        
def thank_you():
    print("Thank you for shopping with us at %s" % site_name)




