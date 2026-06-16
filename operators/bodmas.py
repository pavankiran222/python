###
# Order of Operations
#Python follows the same rules as standard mathematics when deciding which part of a calculation to perform first. The order is often remembered with the acronym BODMAS (or PEMDAS in some countries):
#1. Brackets (Parentheses) — anything inside () is calculated first
#2. Orders (Exponents) — powers like 2 ** 3
#3. Division and Multiplication — evaluated left to right
#4. Addition and Subtraction — evaluated left to right
#Why this matters:
#
#Python
print(2 + 3 * 4)   # 14, NOT 20 — multiplication happens first
print((2 + 3) * 4) # 20 — parentheses force addition first
#Without the parentheses, Python sees 3 * 4 first (giving 12), then adds 2. With parentheses, 2 + 3 is done first (giving 5), then multiplied by 4.
#More examples:

print(10 - 4 / 2)      # 8.0 — division before subtraction: 10 - 2.0 = 8.0
print((10 - 4) / 2)    # 3.0 — subtraction first: 6 / 2 = 3.0
print(2 ** 3 + 1)      # 9 — exponent first: 8 + 1 = 9
print(2 ** (3 + 1))    # 16 — parentheses first: 2 ** 4 = 16

#calculating a discounted price:
price = 100
discount = 0.2
# Correct — subtract discount from 1 first, then multiply
final = price * (1 - discount)   # 80.0

# Wrong — without parentheses, order is different
wrong = price * 1 - discount     # 99.8 (not the intended result)

#Regular division / always gives a decimal:
print(7 / 2)    # 3.5
print(10 / 4)   # 2.5
print(9 / 3)    # 3.0  (still a decimal, even when it divides evenly)

#Floor division // discards the decimal part:
print(7 // 2)   # 3   (not 3.5 — the .5 is thrown away)
print(10 // 4)  # 2
print(9 // 3)   # 3
#Think of floor division as answering: "how many times does the divisor fit in completely?"

#Modulo % gives the remainder:
print(7 % 2)    # 1   (7 = 2×3 + 1 leftover)
print(10 % 4)   # 2   (10 = 4×2 + 2 leftover)
print(9 % 3)    # 0   (9 = 3×3 + 0 leftover — divides evenly)

#Together, // and % are complementary: // tells you the whole result, % tells you what is left over. For example, to convert minutes into hours and minutes:
minutes = 137
hours = minutes // 60    # 2 full hours
remaining = minutes % 60 # 17 minutes left over
print(hours, "hours and", remaining, "minutes")  # 2 hours and 17 minutes

coins = 47
quarters = coins // 25   # 1 quarter (25 cents)
leftover = coins % 25    # 22 cents remaining

#Checking even or odd: n % 2 == 0 is one of the most common Python patterns — it checks whether a number is even (no remainder when divided by 2).