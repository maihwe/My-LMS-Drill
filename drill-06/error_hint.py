""" Implement error_hint(error_type). Return a helpful debugging hint for common Python errors. For NameError return Check variable names and spelling. For TypeError return Check the types before using an operator. For ValueError return Check whether the value can be converted. For ZeroDivisionError return Check that the denominator is not zero. For IndexError return Check the index is inside the valid range. For anything else return Read the traceback carefully."""

def error_hint(error_type):
    if error_type == "NameError":
        return "Check variable names and spelling."
    elif error_type == "TypeError":
        return "Check the types before using an operator."
    elif error_type == "ValueError":
        return "Check whether the value can be converted."
    elif error_type == "ZeroDivisionError":
        return "Check that the denominator is not zero."
    elif error_type == "IndexError":
        return "Check the index is inside the valid range."
    else:
        return "Read the traceback carefully."
        
print(repr(error_hint("NameError")))
print(repr(error_hint("TypeError")))
print(repr(error_hint("ValueError")))
print(repr(error_hint("ZeroDivisionError")))
print(repr(error_hint("IndexError")))
print(repr(error_hint("SyntaxError")))