print("Loading", end="...")   # prints: Loading...   (stays on same line)
print("done")                 # prints: done

# Together on one line:
# Loading...done
print("Mon", "Tue", "Wed", sep=" | ", end="\n---\n")
# Mon | Tue | Wed
# ---
#Both sep and end are what Python calls keyword arguments — named options you pass to a function.
# The default value of sep is a single space, and the default value of end is a newline character (\n).
#Commas in print() automatically add spaces between items. This makes it easy to combine text and variables in your output!