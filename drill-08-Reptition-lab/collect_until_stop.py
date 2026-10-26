""" Implement collect_until_stop(items). Loop through the list and collect items until an item becomes stop after stripping spaces and converting to lowercase. Return the collected items before stop. Use break when stop is found."""
def collect_until_stop(items):
    collected = []

    for item in items:
        if item.strip().lower() == "stop":
            break
        collected.append(items)
    return collected

print(collect_until_stop(["red", "blue", "green"]))
print(collect_until_stop(["one", "STOP", "two"]))
print(collect_until_stop(["A", " stop ", "B"]))
print(collect_until_stop(["stop", "apple"]))
print(collect_until_stop([]))