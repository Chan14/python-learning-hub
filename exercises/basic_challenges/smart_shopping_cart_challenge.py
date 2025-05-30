# Challenge 3: Smart Shopping Cart
# Create a Python function that simulates a simple shopping cart system. The function should:

# Accept a list of tuples, each tuple containing an item name (string), price per unit (float), and quantity (integer).

# Calculate the total price for each item (price × quantity).

# Apply a 10% discount on the total cart price if the total exceeds $100.

# Return a neatly formatted receipt string listing each item, its total price, and the final total price after any discount.

# Example input:
# [
#   ("Apple", 1.5, 10),
#   ("Banana", 0.75, 20),
#   ("Chocolate", 2.0, 5)
# ]
# Example output:
# Apple: 10 × $1.50 = $15.00
# Banana: 20 × $0.75 = $15.00
# Chocolate: 5 × $2.00 = $10.00
# -------------------------------
# Total: $40.00
# (No discount applied)

# If the total were above $100, the receipt should also show the discount applied and the new total.

# Input
# [
#   ("Steak", 25.00, 3),   # 75.00
#   ("Wine Bottle", 30.00, 1), # 30.00
#   ("Cheese", 10.00, 1)   # 10.00
# ]
# Total before discount: $115.00
# Output -
# Steak: 3 × $25.00 = $75.00
# Wine Bottle: 1 × $30.00 = $30.00
# Cheese: 1 × $10.00 = $10.00
# -------------------------------
# Subtotal: $115.00
# Discount Applied: 10% (-$11.50)
# Total after discount: $103.50


def generate_receipt(cart_items: list[tuple[str, float, int]]) -> str:
    order_total = 0
    result = ""
    for cart_entry in cart_items:
        item, price, quantity = cart_entry
        total_price = price * quantity
        result += f"\n{item}: {quantity} × ${price:.2f} = ${total_price:.2f}"
        order_total += total_price
    result += "\n-------------------------------"
    result += f"\nSubtotal: ${order_total:.2f}"
    if order_total > 100:
        discount = 0.1 * order_total
        result += f"\nDiscount Applied: 10% (-${discount:.2f})"
        result += f"\nTotal after discount: ${(order_total - discount):.2f}"
    else:
        result += f"\n(No discount applied)"
    return result


cart = [("Laptop Bag", 45.0, 1), ("Wireless Mouse", 25.0, 2), ("Notebook", 12.5, 3)]

print(generate_receipt(cart))
