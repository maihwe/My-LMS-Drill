""" Implement chunk_list(items, size). Split items into smaller lists of length size. The final chunk may be shorter if there are not enough items left. If size is less than 1, return Invalid size."""

def chunk_list(items, size):
    if size < 1:
        return "Invalid number"

    chunks = []

    for start in range(0, len(items), size):
        chunk = items[start:start + size]
        chunks.append(chunk)

    return chunks

print(chunk_list([1, 2, 3, 4, 5, 6, 7], 3))
# [[1, 2, 3], [4, 5, 6], [7]]

print(chunk_list(["a", "b", "c", "d"], 2))
# [['a', 'b'], ['c', 'd']]

print(chunk_list([1, 2], 5))
# [[1, 2]]

print(chunk_list([], 3))
# []

print(chunk_list([1, 2, 3], 0))
# Invalid size

print(chunk_list([1, 2, 3], -2))
# Invalid size