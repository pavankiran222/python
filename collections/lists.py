ordered_list = ['apple', 'cat', 'banana']
print(ordered_list)
# A list is mutable
ordered_list[0] = 'grape'
print(ordered_list)
# A list can contain duplicate values
duplicate_list = ['apple', 'cat', 'banana', 'apple']
print(duplicate_list)
# A list can contain different data types
mixed_list = ['apple', 42, 3.14, True]
print(mixed_list)
# A list can be nested
nested_list = ['apple', ['cat', 'banana'], 42]
print(nested_list)
# A list can be sorted
sorted_list = sorted(ordered_list)
print(sorted_list)
# A list can be reversed
reversed_list = list(reversed(ordered_list))
print(reversed_list)        