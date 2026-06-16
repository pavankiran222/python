# Python Variables - Advanced Learning Guide
#Naming Conventions
#Python's official style guide (PEP 8) recommends snake_case for variable names: all lowercase letters, with words separated by underscores.
# ===== 1. VARIABLE NAMING CONVENTIONS =====
my_variable = 10  # snake_case (recommended for variables)
MyClass = "class"  # PascalCase (for classes)
CONSTANT_VALUE = 100  # UPPER_CASE (for constants)
_private_var = "private"  # underscore prefix (private convention)

# ===== 2. DATA TYPES AND TYPE CHECKING =====
name = "Pavan"  # str
age = 25  # int
height = 5.9  # float
is_active = True  # bool
colors = ["red", "blue"]  # list
person = {"name": "Pavan", "age": 25}  # dict
coordinates = (10, 20)  # tuple (immutable)
unique_ids = {1, 2, 3}  # set (unique values)

print("=== Type Checking ===")
print(f"Type of name: {type(name)}")
print(f"Type of age: {type(age)}")
print(f"Type of colors: {type(colors)}")

# ===== 3. TYPE CONVERSION =====
print("\n=== Type Conversion ===")
str_number = "42"
int_from_str = int(str_number)
print(f"String '42' to int: {int_from_str}")

float_number = 3.14
int_from_float = int(float_number)
print(f"Float 3.14 to int: {int_from_float}")

number = 100
str_from_number = str(number)
print(f"Number 100 to string: '{str_from_number}'")

# ===== 4. MULTIPLE ASSIGNMENT (UNPACKING) =====
print("\n=== Multiple Assignment ===")
# Tuple unpacking
x, y, z = 1, 2, 3
print(f"x={x}, y={y}, z={z}")

# List unpacking
a, b = [10, 20]
print(f"a={a}, b={b}")

# Swap variables
x, y = y, x
print(f"After swap: x={x}, y={y}")

# ===== 5. MUTABLE vs IMMUTABLE =====
print("\n=== Mutable vs Immutable ===")
# Immutable - string
original_str = "Hello"
modified_str = original_str.replace("Hello", "Hi")
print(f"Original: {original_str}, Modified: {modified_str}")
print(f"Original unchanged (immutable): {original_str}")

# Mutable - list
original_list = [1, 2, 3]
modified_list = original_list
modified_list.append(4)
print(f"Original list: {original_list}")
print(f"Both changed (mutable): {modified_list}")

# ===== 6. REFERENCES vs COPIES =====
print("\n=== References vs Copies ===")
# Shallow copy (reference)
list1 = [1, 2, [3, 4]]
list2 = list1  # This is a reference, not a copy
list2[0] = 99
print(f"After modifying list2, list1: {list1}")

# Deep copy
import copy
list3 = [1, 2, [3, 4]]
list4 = copy.deepcopy(list3)
list4[0] = 99
list4[2][0] = 100
print(f"list3 (unchanged): {list3}")
print(f"list4 (changed): {list4}")

# ===== 7. VARIABLE SCOPE =====
print("\n=== Variable Scope ===")
global_var = "I'm global"

def example_function():
    local_var = "I'm local"
    print(f"Inside function - local_var: {local_var}")
    print(f"Inside function - global_var: {global_var}")

example_function()
print(f"Outside function - global_var: {global_var}")
# print(local_var)  # This would cause an error

# ===== 8. CONSTANTS AND BEST PRACTICES =====
print("\n=== Constants ===")
PI = 3.14159  # Convention: use UPPER_CASE for constants
GRAVITY = 9.8
print(f"Area of circle with radius 5: {PI * 5 ** 2}")

# ===== 9. DYNAMIC TYPING =====
print("\n=== Dynamic Typing ===")
value = 42
print(f"value={value}, type={type(value)}")

value = "Now I'm a string"
print(f"value={value}, type={type(value)}")

value = [1, 2, 3]
print(f"value={value}, type={type(value)}")

# ===== 10. CHECKING IF VARIABLE EXISTS =====
print("\n=== Checking Variables ===")
if 'undefined_var' in locals():
    print("undefined_var exists")
else:
    print("undefined_var doesn't exist")

test_var = 10
if 'test_var' in locals():
    print(f"test_var exists with value: {test_var}")

#Note that Python is case-sensitive: Score, score, and SCORE are three completely different variables. By convention, ALL_CAPS is reserved for constants — values that should never change. Regular variables always use lowercase snake_case.