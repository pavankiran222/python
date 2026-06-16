# Python — indentation defines the block
if True:
    print("This is inside the if block")
    print("So is this line")
print("This is OUTSIDE — no indentation")
# Indentation can be spaces or tabs, but not both
# The standard is 4 spaces per indentation level
# You can use an editor that converts tabs to spaces automatically
# For example, in VS Code, you can set "editor.insertSpaces": true and "editor.tabSize": 4 in your settings.json    

# Two levels of indentation
for i in range(3):            # level 1 — 4 spaces
    if i > 1:                 # level 1 — 4 spaces
        print("More than 1")  # level 2 — 8 spaces
# Incorrect indentation will cause an error
#for i in range(3):
#print(i)  # This will cause an IndentationError because it's not indented 

#Why Whitespace Is Required in Python
#In most programming languages, indentation is purely cosmetic — you can write messy code and it still runs. Python is different: indentation is part of the syntax. Skip it, and you get an error.

#This was a deliberate design choice by Python's creator, Guido van Rossum. His goal was a language that was easy to read and maintain. When indentation is required, every developer's code ends up looking similar — making it much easier to understand code written by someone else.

#Here's a concrete comparison:
# JavaScript — braces show the structure (indentation is optional)
#if (age >= 18)
#{
#print("adult")  # this works even though it looks messy
#}

# Python — indentation IS the structure (no braces needed)
if 100 >= 18:
    print("adult")   # must be indented — no choice