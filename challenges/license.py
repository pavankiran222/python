# def check_license(age, has_license):
#     age = int(input("Please enter your age:"))
#     has_license = input("Do you have a driver's license? (yes/no):").lower()
#     if age >= 18 and has_license == "yes":
#         print("You are allowed to drive.")
#         return True
#     else:
#         print("Sorry, you are not allowed to drive.")
#         return False
# check_license(0, "no")

#The above function can also be coded in a more concise way using a single return statement:
# def check_license(age, has_license):
#     age = int(input("Please enter your age:"))
#     has_license = input("Do you have a driver's license? (yes/no):").lower()
#     print("You are allowed to drive.") if age >= 18 and has_license == "yes" else print("Sorry, you are not allowed to drive.")
# check_license(0, "no")

#The code can also be simplified further by directly returning the boolean expression:
def check_license():
    try:
        age = int(input("Please enter your age:"))
    except ValueError:
        print("Invalid input for age.")
        return False
    try:
        has_license = str(input("Do you have a driver's license? (yes/no):")).lower()
    except ValueError:
        print("Invalid input for driver's license.")
        return False
    if age >= 18 and has_license == "yes":
        print("You are allowed to drive.")
        return True
    else:
        print("Sorry, you are not allowed to drive.")
        return False
check_license()