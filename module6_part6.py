class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0, item_quantity=0, item_description="No description"):
        self.item_name = item_name
        self.item_price = int(item_price)
        self.item_quantity = int(item_quantity)
        self.item_description = item_description

    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${total_cost}")

class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, ItemToPurchase):
        self.cart_items.append(ItemToPurchase)
        print(f"{ItemToPurchase.item_name} has been added to the cart.")

    def remove_item(self, item_name):
        found = False
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                found = True
                print(f"{item_name} has been removed from the cart.")
                break
        if not found:
            print("Item not found in cart. Nothing removed.")

    def modify_item(self, ItemToPurchase):
        # This function is simplified for demonstration; real implementation may vary
        print("Modify item functionality is not implemented in this example.")

    def get_cost_of_cart(self):
        return sum(item.item_price * item.item_quantity for item in self.cart_items)

    def print_total(self):
        print("\nSHOPPING CART TOTAL")
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
        else:
            print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
            print(f"Number of Items: {sum(item.item_quantity for item in self.cart_items)}")
            total_cost = 0
            for item in self.cart_items:
                total_cost += item.item_price * item.item_quantity
                item.print_item_cost()
            print(f"Total: ${total_cost}")

    def print_descriptions(self):
        print("\nSHOPPING CART ITEM DESCRIPTIONS")
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions:")
        for item in self.cart_items:
            print(f"{item.item_name}: {item.item_description}")

def print_menu(shoppingCart):
    menu_options = {
        'a': "Add item to cart",
        'r': "Remove item from cart",
        'c': "Change item quantity",
        'i': "Output items' descriptions",
        'o': "Output shopping cart",
        'q': "Quit"
    }

    def add_item_to_cart():
        item_name = input('Enter the item name: ')
        item_price = int(input('Enter the item price: '))
        item_quantity = int(input('Enter the item quantity: '))
        item_description = input('Enter the item description: ')
        new_item = ItemToPurchase(item_name, item_price, item_quantity, item_description)
        shoppingCart.add_item(new_item)

    def remove_item_from_cart():
        item_name = input('Enter the item name to remove: ')
        shoppingCart.remove_item(item_name)

    while True:
        print("\nMENU")
        for key, value in menu_options.items():
            print(f"{key} - {value}")
        choice = input("Choose an option: ")
        
        if choice == 'a':
            add_item_to_cart()
        elif choice == 'r':
            remove_item_from_cart()
        elif choice == 'c':
            print("Change item quantity option is selected.")
            # Implement change item quantity
        elif choice == 'i':
            shoppingCart.print_descriptions()
        elif choice == 'o':
            shoppingCart.print_total()
        elif choice == 'q':
            print("Quit")
            break
        else:
            print("Invalid option. Please try again.")

def main():
    shopping_cart = ShoppingCart("John Doe", "February 1, 2020")
    print_menu(shopping_cart)

if __name__ == "__main__":
    main()