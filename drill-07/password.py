"""Implement password_strength(password). Return Weak if the password has fewer than 8 characters. Return Medium if it has at least 8 characters but does not contain both letters and digits. Return Strong if it has at least 8 characters and contains at least one letter and at least one digit. Students may need to research isalpha and isdigit."""
def password_strength(password):
    if len(password) < 8:
        return "Weak"

    has_letter = False
    has_digit = False

    for characters in password:
        if characters.isalpha():
            has_letter = True
        if characters.isdigit():
            has_digit = True

    if has_digit and has_letter:
        return "Strong"
    else:
        return "Medium"

print(password_strength("abc12"))
print(password_strength("password"))
print(password_strength("12345678"))
print(password_strength("hello123"))
print(password_strength("Hello2026"))