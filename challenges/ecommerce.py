#Create an empty cart: Initialize an empty list called shopping_cart outside of your functions.
#Function 1: add_to_cart(item_name)
#Check if the item_name exists in the store_inventory (using membership operators).
#If it exists, append that string to your shopping_cart list and print a success message.
#If it doesn't exist, print an error message telling them it's out of stock.
#Function 2: calculate_total()
#This function should loop through the shopping_cart list.
#Look up each item's price in the store_inventory.
#Sum up the prices, apply a 7% sales tax using arithmetic operators, and return the final total.
#The Interactive Loop (input)
#Write a simple loop that asks the user: "What would you like to buy? (or type 'checkout' to finish): "
#If they type an item, call add_to_cart().
#If they type 'checkout', break the loop, call calculate_total(), and print out their final bill formatted nicely (e.g., "Your final total with tax is: $X.XX").

store_inventory = {
    "laptop": 899.99,
    "headphones": 149.50,
    "mouse": 24.99,
    "keyboard": 75.00
}
shopping_cart = []
def add_to_cart(item_name: str) -> None:
    if item_name in store_inventory:
        shopping_cart.append(item_name)
        print(f"{item_name} has been added to your cart.")
    else:
        print(f"Sorry, {item_name} is out of stock.")
def calculate_total() -> float:
    total = sum(store_inventory[item] for item in shopping_cart)
    total_with_tax = total * 1.07  # Apply 7% sales tax
    return total_with_tax
def main():
    while True:
        item_name = input("What would you like to buy? (or type 'checkout' to finish): ").lower()
        if item_name == 'checkout':
            break
        add_to_cart(item_name)
    final_total = calculate_total()
    print(f"Your final total with tax is: ${final_total:.2f}")
if __name__ == "__main__":    
    main()