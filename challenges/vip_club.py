# Challenge 1: The VIP Club Bouncer
# Concepts: input(), Functions, Logical Operators (and, or, not)
# Write a function called check_entry that takes no arguments but prompts the user for two pieces of information:
# Their age (as an integer).
# Whether they are on the guest list (expecting "yes" or "no").
# The Rules: * To get in, the user must be 21 or older AND on the guest list.
# Twist: If they are 25 or older, they get in automatically, regardless of the guest list.
# The function should return True if they are allowed entry, and False otherwise.

#Check Age and Guest List
def check_entry():
    age = int(input("Please enter your age:"))
    guest_list = input("Are you on the guest list? (yes/no):").lower()
    if age >= 25:
        print("Welcome to the VIP club! You get in automatically.")     
        return True
    elif age >= 21 and guest_list == "yes":
        print("Welcome to the VIP club! You are on the guest list.")
        return True
    else:
        print("Sorry, you are not allowed entry.")
        return False
check_entry()