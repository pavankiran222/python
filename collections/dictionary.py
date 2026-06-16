dictionary={
    "name":"John",
    "age":30,
    "city":"New York"
}
print(dictionary)
# A dictionary maintains insertion order
print(dictionary["name"])
# A dictionary is mutable
dictionary["age"] = 31
print(dictionary)
# A dictionary can contain duplicate values
dictionary["hobby"] = "reading"
dictionary["hobby"] = "writing"
print(dictionary)
# A dictionary can contain different data types
dictionary["is_student"] = False
print(dictionary)
# A dictionary can be nested
nested_dictionary = {
    "name": "John",
    "age": 30,
    "address": {        
        "street": "123 Main St",
        "city": "New York",
        "state": "NY"
    }
}
print(nested_dictionary)
# A dictionary can be sorted by keys
sorted_dictionary = dict(sorted(dictionary.items()))
print(sorted_dictionary)
# A dictionary can be sorted by values
#sorted_by_values = dict(sorted(dictionary.items(), key=lambda item: item[1]))
#print(sorted_by_values) 
# A dictionary can be reversed
reversed_dictionary = dict(reversed(dictionary.items()))
print(reversed_dictionary)