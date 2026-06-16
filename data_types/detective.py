from collections import defaultdict
mixed_bag = [42, "Python", 3.14, True, "AI", False, 100, [1, 2, 3]]
type_counts = defaultdict(int)

for item in mixed_bag:
    if isinstance(item, bool):
        type_counts['bool'] += 1
    else:
        type_counts[type(item).__name__] += 1

print(dict(type_counts))