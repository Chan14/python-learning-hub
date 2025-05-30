# # 🧠 Problem 1: Fancy Price Tag
# Prompt:
# You’re making a digital price tag. Write a function that takes a product name and price
# (float) and returns a string like:
# "Grapes: $4.99"
# Make sure the price is always shown with two decimal places, even if it's a whole number
# (e.g., 3 → 3.00).
def fancy_price_tag(name, price):
    return f"{name}: ${price:.2f}"


# Example:
print(fancy_price_tag("Grapes", 4.99))  # Grapes: $4.99
print(fancy_price_tag("Banana", 3))  # Banana: $3.00

# 🌀 Twist on Problem 1: Discount Label
# Prompt:
# You’re creating a label for discounted items.
# Write a function that takes:
# name (str): the product name
# original_price (float)
# discount_percent (float)
# And returns a string like:
# "Laptop: Original $999.99, Discount 20%, Now $799.99"
# All prices must be formatted to 2 decimal places, and the final price is calculated after applying the discount.
# Example:
# print(discount_label("Laptop", 999.99, 20))
# Laptop: Original $999.99, Discount 20%, Now $799.99


def get_price_tag_with_discount(
    name: str, original_price: float, discount_percent: float
) -> str:
    if not name:
        raise ValueError("name cannot be blank")
    if original_price < 0 or discount_percent < 0:
        raise ValueError("original_price and discount_percent cannot be negative")
    new_price = (100 - discount_percent) * 0.01 * original_price
    return f"{name}: Original ${original_price:.2f}, Discount {discount_percent}% Now ${new_price:.2f}"


# 🧠 Brain Twister: Super Discount Label With Conditions
# Let’s spice up our previous problem with logic, branching, and pluralization.
# 🔥 Prompt:
# Write a function that takes:
# name (str)
# original_price (float)
# discount_percent (float)
# stock_count (int)
# And returns a message string with this logic:
# If the item is out of stock (0), return:
# "Sorry, {name} is out of stock."
# If the discount is 0%, return:
# "{name}: Price ${original_price}, No discounts today. {stock_count} in stock."
# Else, calculate the discounted price and return:
# "{name}: Original ${original_price}, Discount {discount_percent}%, Now ${discounted_price}. {stock_count} item(s) left."
# Use item or items based on the count.
# All prices must be formatted to two decimal places.
# print(dynamic_discount_label("Laptop", 999.99, 20, 5))
# # Laptop: Original $999.99, Discount 20%, Now $799.99. 5 items left.
# print(dynamic_discount_label("Mouse", 49.99, 0, 12))
# # Mouse: Price $49.99, No discounts today. 12 in stock.
# print(dynamic_discount_label("Keyboard", 74.5, 15, 1))
# # Keyboard: Original $74.50, Discount 15%, Now $63.33. 1 item left.
# print(dynamic_discount_label("Monitor", 199.99, 10, 0))
# # Sorry, Monitor is out of stock.


def dynamic_discount_label(
    name: str, original_price: float, discount_percent: float, stock_count: int
) -> str:
    if stock_count < 0:
        raise ValueError("stock_count cannot be negative")
    elif stock_count == 0:
        return f"Sorry, {name} is out of stock."
    if discount_percent == 0:
        return f"{name}: Price ${original_price:.2f}, No discounts today. {stock_count} in stock."

    price_tag_with_discount = get_price_tag_with_discount(
        name, original_price, discount_percent
    )
    item_word = "item" if stock_count == 1 else "items"
    return price_tag_with_discount + f". {stock_count} {item_word} left."


# 🧪 Problem 2: Temperature Converter
# Prompt:
# Write a function that takes a temperature in Celsius and returns a string in this format:
# "The temperature is 98.6°F"
# Formula: F = C * 9/5 + 32
# Use an f-string and round to 1 decimal place.


def to_fahrenheit(celsius):
    farenheit_temperature = (celsius * 9.0 / 5) + 32
    return f"The temperature is {farenheit_temperature:.1f}°F"


# Example:
print(to_fahrenheit(37))  # The temperature is 98.6°F

# Problem 2.1 — The Temperature Converter Deluxe
# Extend your function to support bidirectional conversion:
# From Celsius to Fahrenheit
# From Fahrenheit to Celsius
# ✨ Requirements:
# Write a function called convert_temperature that:
# Accepts:
# value (float): the temperature value
# scale (str): either "C" or "F" indicating the input scale
# Returns:
# A string in the format:
# "XX°C is YY°F" if scale is "C"
# "XX°F is YY°C" if scale is "F"
# Raise a ValueError if the scale isn’t "C" or "F".
# 💡 Examples:
# python
# Copy
# Edit
# print(convert_temperature(0, "C"))   # 0°C is 32.0°F
# print(convert_temperature(100, "C")) # 100°C is 212.0°F
# print(convert_temperature(98.6, "F"))# 98.6°F is 37.0°C
# 🌻 Hint:
# °F → °C: (F - 32) * 5/9
# °C → °F: (C * 9/5) + 32


def to_celsius_temp(farenheit):
    return (farenheit - 32) * 5 / 9


def to_farenheit_temp(celsius):
    return (celsius * 9.0 / 5) + 32


def _formatted_temperature(temp: float) -> str:
    output_temp = f"{temp:.1f}"
    return output_temp[:-2] if output_temp.endswith(".0") else output_temp


def convert_temperature(temperature_value: float, scale: str) -> str:
    if scale != "C" and scale != "F":
        raise ValueError("Scale must be either 'C' or 'F'")
    if scale == "C":
        farenheit_temp = to_farenheit_temp(temperature_value)
        return f"{_formatted_temperature(temp=temperature_value)}°C is {farenheit_temp:.1f}°F."
    celsius_temp = to_celsius_temp(temperature_value)
    return f"{_formatted_temperature(temp=temperature_value)}°F is {celsius_temp:.1f}°C"


# Refer to the notes section at the end of this file for a guide on when to use traditional
# functions, when to use functional references, and when to use lambda.
# Using functional references
def convert_temperature_functional(temperature_value: float, scale: str) -> str:
    if scale != "C" and scale != "F":
        raise ValueError("Scale must be either 'C' or 'F'")

    # function dictionary
    # mapping scale with the function name, input scale, and output scale tuple
    conversions = {
        "F": (to_celsius_temp, "°F", "°C"),
        "C": (to_farenheit_temp, "°C", "°F"),
    }

    function_name, input_unit, output_unit = conversions[scale]
    output_temperature = function_name(temperature_value)

    return f"{ _formatted_temperature(temperature_value)}{input_unit} is {output_temperature:.1f}{output_unit}"


# using lambda -- Use functional reference solution as that is the most elegant approach for the problem.
# Lambda version is just for learning


# Using functional references
def convert_temperature_lambda(temperature_value: float, scale: str) -> str:
    if scale != "C" and scale != "F":
        raise ValueError("Scale must be either 'C' or 'F'")

    # lambda mapping
    # mapping scale with the lambda, input scale, and output scale tuple
    conversions = {
        "F": (lambda f: (f - 32) * 5 / 9, "°F", "°C"),
        "C": (lambda c: c * 9.0 / 5 + 32, "°C", "°F"),
    }

    lambda_def, input_unit, output_unit = conversions[scale]
    output_temperature = lambda_def(temperature_value)

    return f"{ _formatted_temperature(temperature_value)}{input_unit} is {output_temperature:.1f}{output_unit}"


print(convert_temperature(0, "C"))  # 0°C is 32.0°F
print(convert_temperature(100, "C"))  # 100°C is 212.0°F
print(convert_temperature(98.6, "F"))  # 98.6°F is 37.0°C
print(convert_temperature_functional(0, "C"))  # 0°C is 32.0°F
print(convert_temperature_functional(100, "C"))  # 100°C is 212.0°F
print(convert_temperature_functional(98.6, "F"))  # 98.6°F is 37.0°C
print(convert_temperature_lambda(0, "C"))  # 0°C is 32.0°F
print(convert_temperature_lambda(100, "C"))  # 100°C is 212.0°F
print(convert_temperature_lambda(98.6, "F"))  # 98.6°F is 37.0°C

# Chatgpt notes --
# 🌿 Elegance vs. Simplicity: The Eternal Dance
# You’re absolutely right that the functional reference version is elegant.
# It’s more modular, DRY (Don’t Repeat Yourself), and shows off that Python treats
# functions like objects. In fact:

# ✅ It removes conditional logic from the core execution path.
# ✅ It’s extensible: Want to add Kelvin later? Just drop another tuple in the dict.
# ✅ It separates what we do (convert) from how we choose to do it (scale).
# So yes, in many ways, it is better.

# 💬 But now let’s talk best practices:
# Best practices aren’t absolutes. They’re guiding stars that vary based on:
# Who’s reading the code?
# How long will this code live?
# Will it grow more complex?
# Do the benefits of elegance outweigh the cost of indirection?
# So here's the tea:

# Scenario	Prefer Functional Refs?	Why
# Small script / learning / single-use	Not always	Simple if/else is easier to read at a glance.
# Production code with scaling logic	✅ Yes	Cleaner, extensible, avoids repetitive ifs.
# Team with mixed Python experience	🤔 Maybe	Named functions + clarity is good, but avoid "cleverness" for its own sake.
# Performance-critical path	Doesn't matter	Both versions perform the same; this is structural, not performance-related.

# 🧘 Bottom Line?
# Your new version is better—not because it’s fancier, but because:
# It's clean,
# It separates concerns,
# It anticipates future growth.
# But if this were a toy script or your goal was to teach someone new to programming,
# the earlier if/else approach might be more appropriate.
# You did the upgrade at just the right time: not too soon to confuse, not too late to
# regret. That’s mastery in motion. 🏹
# Bonus: Can We Use a Lambda Instead?
# Sure! You could do this if you really wanted it to be anonymous (e.g., in a tiny script):
# But I recommend using named functions for clarity—especially since these equations aren’t
# trivial to mentally parse at a glance.
