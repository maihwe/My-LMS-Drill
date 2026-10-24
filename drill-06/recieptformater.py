""" **Implement receipt_formatter(name, quantity, price). Calculate subtotal as quantity multiplied by price. Calculate tax as 7.5 percent of subtotal. Calculate total as subtotal plus tax. Return a four-line report with labels Customer, Subtotal, Tax, and Total. Round subtotal, tax, and total to 2 decimal places.**"""

def receipt_formatter(name, quantity, price):
    quantity = float(quantity)
    price = float(price)

    subtotal = quantity * price
    tax = round(subtotal * 0.075, 2)
    total = round(subtotal + tax, 2)

    def format_amount(amount):
        result = f"{amount:.2f}".rstrip("0").rstrip(".")
        if "." not in result:
            result += ".0"
        return result

    return (
        f"Customer: {name}\n"
        f"Subtotal: {format_amount(subtotal)}\n"
        f"Tax: {format_amount(tax)}\n"
        f"Total: {format_amount(total)}"
    )
print(receipt_formatter("Ada", 2, 100))
print(receipt_formatter("Tunde", 3, 25.5))
print(receipt_formatter("Sam", "2", "0.50"))

