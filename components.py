# CLASSES AND METHODS
class Store():
    def __init__(self, name):
        """
        Initializes a new store with a name.
        """
        self.name= name
        self.products= []

    def add_product(self, product):

        """
        Adds a product to the list of products in this store.
        """
        self.products.append(product)


    def print_products(self):
        """
        Prints all the products of this store in a nice readable format.
        """
        print("%s:" % self.name)
        [print("-",self.product) for products in self.products]
        print()


class Product():
    def __init__(self, name, description, price):
        """
        Initializes a new product with a name, a description, and a price.
        """
        self.name= name
        self.description= description
        self.price= price 

    def __str__(self):
        return "Product Name: %s\n\tDescription: %s\n\tPrice: %sKD"%(self.name,self.description,self.price)
        

class Cart():
    total=0
    def __init__(self,products):

        self.products= []

    def add_to_cart(self, product):
        """
        Adds a product to this cart.
        """
        self.products.append(product)

    def get_total_price(self):
        """
        Returns the total price of all the products in this cart.
        """
        price=0
        for product in self.products:
            price += product.price
            
        return price 
    def print_receipt(self):
        """
        Prints the receipt in a nice readable format.
        """
        print ("Here's your receipt: ")
        for product in self.products:
            print(product)
            print()
        print("Your total price is: KD%s" %self.get_total_price())

    def checkout(self):
        """
        Does the checkout.
        """
        print ("---------------------")
        self.print_receipt()
        confirm= input("Confirm? (yes/no)")
        if confirm.lower()== "yes" or confirm.lower()== "y":
            self.products= []
            print("Your order has been placed.")
        else:
            print("Your order has been cancelled.")