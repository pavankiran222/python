mixed_bag = [42, "Python", 3.14, True, "AI", False, 100, [1, 2, 3]]

#Initialize counters
int_count = 0
str_count = 0
float_count = 0
bool_count = 0
list_count = 0

#Iterate through the mixed bag and count each data type
for item in mixed_bag:
    if isinstance(item, bool):
        bool_count += 1
    elif isinstance(item, int):
        int_count += 1
    elif isinstance(item, str):
        str_count += 1
    elif isinstance(item, float):
        float_count += 1
    elif isinstance(item, list):
        list_count += 1

#Print the results
print(f"Number of integers: {int_count}")
print(f"Number of strings: {str_count}")
print(f"Number of floats: {float_count}")
print(f"Number of booleans: {bool_count}")
print(f"Number of lists: {list_count}")