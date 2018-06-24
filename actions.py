
# UTILS AND FUNCTIONALITY
from data import stores
from components import Cart

site_name = "www.carted.com"  # Give your site a name


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

    for store in stores:
        if store.name.lower() == store_name.lower():
            return store
        
#    else:
#        print ("Please pick a valid store name")
        
            
    
def pick_store():
    
    """
    prints list of stores and prompts user to pick a store.
    """
    print_stores()
    store_name= input("Pick a store by typing its name. Or type \"checkout\" to pay your bills and say your goodbyes.\n")
    if store_name.lower() != "checkout":
        picked_store= get_store(store_name)
        return picked_store
 

    
    
def pick_products(cart,picked_store):
    """
    prints list of products and prompts user to add products to cart.
    """
    print()
    for product in picked_store.products:
        print(product.name)
    picked_products= input("Add items to your cart by typing the product name exactly as it was spelled above.\nType \"back\" to go back to the main menu where you can checkout.\n")
        
    
    while picked_products.lower() != "checkout":
            if picked_products.lower() == product.name.lower():
                cart.add_to_cart(product)
                print("Item added to cart!")
                picked_products =input("Anything else? Type any additional product or type \"checkout\" to exit or \"back\" to return to main menu.\n" )
            else:
                print("Invalid product.")
                picked_products= input("Please enter a valid product name as spelled above. Enter \"checkout\" to exit or \"back\" to return to main menu.\n")
            #prompts user to enter another store to shop there ??  
            while picked_products.lower() == "back":
                pick_store()
                shop()
                
          

def shop():

    """
    The main shopping functionality
    """
    cart= Cart([])
    picked_store = pick_store()
    while not picked_store:
        print("PICK STORE")
        picked_store= pick_store()
    pick_products(cart, picked_store)
    cart.checkout()
    
        
def thank_you():
    print("Thank you for shopping with us at %s!" % site_name)




