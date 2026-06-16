"""
This function calculates the final price
  including tax and any applicable discounts.
 It expects the price in dollars and the tax rate as a decimal.
 def calculate_price(price, tax_rate):
     return price * (1 + tax_rate)
 print(calculate_price(100, 0.07))  # Output: 107.0
Each line is clearly a comment, and most code editors let you highlight several lines and comment them all at once with a keyboard shortcut (usually Ctrl+/ or Cmd+/).
"""
def calculate_price(price=0, tax_rate=0, discount=0):
    return price * (1 + tax_rate) - discount
print(calculate_price(100, 0.07))          # Output: 107.0 (no discount)
print(calculate_price(100, 0.07, 10))  # Output: 97.0 (with discount)

"""In this function, we have three parameters: price, tax_rate, and discount. Each parameter has a default value of 0. 
This means that if you call calculate_price without providing a value for any of these parameters, it will use the default value. 
For example, calculate_price() will return 0, while calculate_price(100) will return 100 (since tax_rate and discount default to 0). This allows for flexible function calls while still providing sensible defaults."""

"""
This block of text is technically a string, not a comment.
Python evaluates it but discards the result because it is
not assigned to anything.
This works, but it is not a true comment — it is a string literal that Python creates and immediately throws away. 
The important exception is when triple-quoted strings appear at the very start of a function, class, or file. 
In that position they become a docstring formal documentation that tools and the help() function can read.
"""