""" Implement skip_evens(start, end). Return a list of odd numbers from start to end inclusive. Use continue to skip even numbers. If start is greater than end, return an empty list."""
def skip_evens(start, end):
    odd_numbers = []

    for number in range(start, end + 1):
        if number % 2 == 0:
            continue
        odd_numbers.append(number)
    return odd_numbers

print(skip_evens(2, 9))   # [3, 5, 7, 9]
print(skip_evens(1, 5))   # [1, 3, 5]
print(skip_evens(4, 4))   # []
print(skip_evens(7, 3))   # []
print(skip_evens(-3, 3))  # [-3, -1, 1, 3]