""" **Implement initials_badge(full_name). Remove leading and trailing spaces, split the name into words, take the first character of each word, convert each initial to uppercase, and return the initials joined with dots. The returned badge should end with a dot.**"""

def initials_badge(full_name):
    full_name = full_name.strip()
    words = full_name.split()

    initials = []

    for word in words:
        initials.append(word[0].upper())

    return ".".join(initials) + "."
    
print(initials_badge("Ada Lovelace"))
print(initials_badge("Mary Jane Watson"))