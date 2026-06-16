# A set is unordered
unordered_set = {'apple', 'cat', 'banana'}
#print(unordered_set.sort())  # This will raise an error because sets do not support indexing or sorting
print(unordered_set) 
# Output might be: {'banana', 'apple', 'cat'} 
# Python just shuffles them into memory however it wants!



# A set is mutable
unordered_set.add('grape')
print(unordered_set)
# Output might be: {'banana', 'grape', 'apple', 'cat'}