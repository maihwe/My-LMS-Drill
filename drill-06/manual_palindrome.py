""" **Implement manual_palindrome(text). Ignore spaces and letter case. Return true if the cleaned text reads the same forward and backward, otherwise return false. Do not use slicing shorthand or reversed. Students may need to research manual string reversal.**"""

def manual_palindrome(text):
    text = text.lower()
    text = text.replace(" ", "")

    reversed_text = ""

    for i in range(len(text) - 1, -1, -1):
        reversed_text += text[i]

    return text == reversed_text
    
print(manual_palindrome("Race Car"))
print(manual_palindrome("hello"))
print(manual_palindrome("nurses run"))
print(manual_palindrome("Python"))