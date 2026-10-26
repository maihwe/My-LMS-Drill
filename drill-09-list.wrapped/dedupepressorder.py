""" Implement dedupe_preserve_order(items). Return a new list with duplicate values removed while keeping the first time each value appeared. Do not use set for this challenge."""

def dedupe_preserve_order(items):
    unique = []

    for item in items:
        if item not in unique:
            unique.append(item)
    return unique

print(dedupe_preserve_order([3, 1, 3, 2, 1, 4, 2]))
# [3, 1, 2, 4]

print(dedupe_preserve_order(["a", "b", "a", "c", "b"]))
# ['a', 'b', 'c']

print(dedupe_preserve_order([1, 2, 3]))
# [1, 2, 3]

print(dedupe_preserve_order([5, 5, 5]))
# [5]

print(dedupe_preserve_order([]))
# []