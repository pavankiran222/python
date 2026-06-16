# menu: dict[str, float] = {
#     "Espresso": 2.5,
#     "Latte": 3.5,
#     "Cappuccino": 3.0,
#     "Mocha": 4.0,
#     "Tea": 2.0
# }
# def order_drink(drink_name: str) -> str:
#     if drink_name in menu:
#         print(f"You ordered a {drink_name}.")
#         return drink_name
#     else:
#         print("Sorry, that drink is not available.")
#         return "Invalid drink"
# def calculate_total(order: list[str]) -> float:
#     total = 0.0
#     for drink in order:
#         if drink in menu:
#             total += menu[drink]
#         else:
#             print(f"Warning: {drink} is not on the menu and will be skipped.")
#     return total
# def main():
#     order = []
#     while True:
#         drink_name = input("Enter the name of the drink you want to order (or 'done' to finish): ")
#         if drink_name.lower() == 'done':
#             break
#         ordered_drink = order_drink(drink_name)
#         if ordered_drink != "Invalid drink":
#             order.append(ordered_drink)
#     total_cost = calculate_total(order)
#     print(f"Your total is: ${total_cost:.2f}")
# if __name__ == "__main__":    main()

# The Digital Coffee Shop
# Concepts: Dictionaries, Membership Operators (in), Functions
# Create a dictionary called menu where the keys are drink names (strings) and the values are prices (floats). Populated it with at least 3 items (e.g., "latte": 4.50).
# Write a function called order_drink(drink_name) that:
# Checks if the drink_name exists in your menu dictionary.
# If it does, prints: "That will be $X.XX." (substituting the actual price).
# If it doesn't, prints: "Sorry, we don't serve that here!"
# Test your function by calling it with a valid drink name and an invalid drink name.
menu: dict[str, float] = {
    "espresso": 2.5,
    "latte": 3.5,
    "cappuccino": 3.0
}
def order_drink(drink_name: str) -> None:
    if drink_name in menu:
        print(f"That will be ${menu[drink_name]:.2f}.")
    else:
        print("Sorry, we don't serve that here!")
# Test the function with a valid drink name and an invalid drink name
drink_name = input("Enter the name of the drink you want to order: ").lower()
order_drink(drink_name)