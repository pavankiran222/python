# The ATM Bank Simulator
# Goal: Build a simple, interactive ATM machine script that uses functions to manage a user's account balance, enforces boundaries (like preventing negative balances), and safely handles invalid user inputs.
# The Setup Data
# Start with a starting balance variable outside of your functions:
# account_balance = 500.00  # Starting balance
# Your Requirements
# Global State Management: * Remember to use the global keyword inside your functions if you plan on modifying account_balance directly.
# Function 1: check_balance()
# Simply prints the current balance formatted nicely (e.g., "Your current balance is: $500.00").
# Function 2: deposit(amount)
# Validates that the amount is greater than 0.
# If valid, adds it to account_balance and prints the new balance. Otherwise, prints an error message.
# Function 3: withdraw(amount)
# Checks if amount is greater than the available account_balance.
# If the user has enough money, deducts the amount and prints the success message.
# If they don't, prints "Error: Insufficient funds!"
# The Interactive Menu (input)
# Create a loop that displays a menu:
# Plaintext
# 1. Check Balance
# 2. Deposit Money
# 3. Withdraw Money
# 4. Exit
# Prompt the user for their choice (1-4).
# The Twist: Use try/except blocks when asking for numbers (like deposit or withdrawal amounts) so that if a user accidentally types a word like "hundred", the program doesn't crash with a ValueError.