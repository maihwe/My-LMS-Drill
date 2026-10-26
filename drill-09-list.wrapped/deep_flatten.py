""" Implement deep_flatten(items). Return a flat list containing every non-list value from items, no matter how deeply nested the lists are. Students may need to research recursion. Preserve the left-to-right order."""
def deep_flatten(items):
    result = []

    for item in items:
        if isinstance(item, list):
            result.append(deep_flatten(item))
        else:
            result.append(item)
    return result
print(deep_flatten([1, [2, 3], [4, [5, 6]]]))
# [1, 2, 3, 4, 5, 6]

print(deep_flatten([[["hello"]], "world"]))
# ['hello', 'world']

print(deep_flatten([1, 2, 3]))
# [1, 2, 3]

print(deep_flatten([[], [1, []], [[2]]]))
# [1, 2]

print(deep_flatten([]))
# []