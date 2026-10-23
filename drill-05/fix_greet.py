def fix_greeting(name):
    return f"Hello, {name}."

print(fix_greeting("Mathias"))

"""Implement next_age(age_text). The function receives age as text. Convert it to an integer and return the age next year. This fixes the common bug where text is used like a number."""

def next_age(age_text):
    return int(age_text) + 1
print(next_age("20"))


"""Implement safe_divide(a, b). Return a divided by b rounded to 2 decimal places. If b is zero, return Cannot divide by zero. This fixes the common ZeroDivisionError bug.
"""

def safe_divide(a, b):
    if b == 0:
        return "cannot divide by zero"
    return round(a / b, 2)


print(safe_divide(10, 3))
print(safe_divide(10, 2))
print(safe_divide(10, 0))

"""  Implement grade_label(items, index). Return the item at the given index. If the index is outside the list, return Index out of range. Negative indexes should also return Index out of range for this challenge."""

def grade_label(items, index):
    if index < 0 or index >= len(items):
        return "Index out of range"
    return items[index]
items = ["orange", "Pawpaw", "Apple", "Manage"]
print(grade_label(items, 0))
print(grade_label(items, 2))
print(grade_label(items, 3))
print(grade_label(items, -1))

"""Implement grade_label(score). Return A for scores from 90 to 100, B for scores from 80 to 89, C for scores from 70 to 79, and F for scores below 70. If the score is less than 0 or greater than 100, return Invalid score. This fixes common comparison and branch-order bugs.
""" 
def grade_label(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "F"

print(grade_label(100))
print(grade_label(89))
print(grade_label(70))
print(grade_label(45))
print(grade_label(101))
print(grade_label(-2))