# The Stats Calculator
# Concepts: Lists, Arithmetic Operators, Built-in Functions
# Write a function called analyze_scores(scores) that takes a list of numbers (representing test scores).
# Inside the function, calculate and return three things in a single dictionary:
# The total number of scores (use len()).
# The highest score (use max()).
# The average score (calculate this using sum() and len()).
# Test it with: analyze_scores([85, 90, 78, 92, 100])

# def analyze_score(score):
#     number = len(score)
#     highest = max(score)
#     average = sum(score) / len(score)
#     return f"Score Analysis: Number of Scores: {number}, Highest Score: {highest}, Average Score: {average:.2f}"
# score = [int(x) for x in input("Enter scores separated by spaces: ").split()]
# print(analyze_score(score))

#The above can also be done using a dictionary as follows:
def analyze_score(score):
    analysis = {
        "number_of_scores": len(score),
        "highest_score": max(score),
        "average_score": sum(score) / len(score)
    }
    return analysis
score = [int(x) for x in input("Enter scores separated by spaces: ").split()]
print(analyze_score(score))