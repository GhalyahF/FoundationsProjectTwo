# CLASSES AND METHODS
class Store():
    def __init__(self, name):
        """
        Initializes a new store with a name.
        """
        self.name= name

    def add_product(self, product):

        """
        Adds a product to the list of products in this store.
        """
        self.products= []
        self.products.append(product)


    def print_products(self):
        """
        Prints all the products of this store in a nice readable format.
        """
        [print("-",self.product) for products in self]


class Product():
    def __init__(self, name, description, price):
        """
        Initializes a new product with a name, a description, and a price.
        """
        self.name= name
        self.description= description
        self.price= price 

    def __str__(self):
        print(" %s,%s,%s")%(self.name,self.description,self.price)
        

class Cart():
    total=0
    def __init__(self,products):

        self.products= []

    def add_to_cart(self, product):
        """
        Adds a product to this cart.
        """
        self.append(product)

    def get_total_price(self):
        """
        Returns the total price of all the products in this cart.
        """
        total=0
        for product in self.products:
            price= product[1]
            total += price 
    def print_receipt(self):
        """
        Prints the receipt in a nice readable format.
        """
        print("Total: $%.2f")%self.price

    def checkout(self,paid):
        """
        Does the checkout.
        """
        print ("Checking out. You have a total of %.02f worth of items in your cart" % (Cart.price))
        return print_receipt()