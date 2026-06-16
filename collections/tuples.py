# A tuple is ordered
ordered_tuple = ('apple', 'cat', 'banana')
print(ordered_tuple[2])
# A tuple is immutable
# ordered_tuple[0] = 'grape'  # This will raise a TypeError
# A tuple can contain duplicate values
duplicate_tuple = ('apple', 'cat', 'banana', 'apple')
# duplicate_tuple = duplicate_tuple.sort()  # This will raise an error because tuples do not support sorting
print(duplicate_tuple)
# A tuple can contain different data types
mixed_tuple = ('apple', 42, 3.14, True)
print(mixed_tuple)
# A tuple can be nested
nested_tuple = ('apple', ('cat', 'banana'), 42)
print(nested_tuple)