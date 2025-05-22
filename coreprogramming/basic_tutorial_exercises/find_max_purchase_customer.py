# Exercise: Finding the Customer With the Most Purchases.
# Use what you've learned so far to find the customer who has made the most purchases in
# a week.

# Problem statement
# You have been provided with a groceries dictionary that contains the names of the
# customer as the key and the number of items they bought each day in a week as a list of
# values.

# groceries = {
#     "James": [10, 2, 5, 7, 9, 4, 6],
#     "Tom": [1, 12, 3, 0, 1, 2, 5],
#     "Sam": [9, 5, 4, 3, 2, 1, 3],
# }

# Therefore, your task is to write the most_purchases() function. This function takes
# in the groceries dictionary and returns the name of customer who has made the most p
# urchases in a week, along with their total purchase.

# Input :
# groceries = {
#     "James": [10, 2, 5, 7, 9, 4, 6],
#     "Tom": [1, 12, 3, 0, 1, 2, 5],
#     "Sam": [9, 5, 4, 3, 2, 1, 3],
# }
# Output
# ("James", 43)

groceries = {
    "James": [10, 2, 5, 7, 9, 4, 6],
    "Tom": [1, 12, 3, 0, 1, 2, 5],
    "Sam": [9, 5, 4, 3, 2, 1, 3],
}


def most_purchases(groceries):
    max_purchase = (None, 0)
    for customer, purchase in groceries.items():
        total_purchase = sum(purchase)
        if total_purchase > max_purchase[1]:
            max_purchase = (customer, total_purchase)
    return max_purchase


print(most_purchases(groceries))


# Using lambda
def most_purchases_using_lambda(groceries):
    customer, purchases = max(groceries.items(), key=lambda item: sum(item[1]))
    return (customer, sum(purchases))


print(most_purchases_using_lambda(groceries))


# Using functional reference
def get_total_purchase(item):
    return sum(item[1])


def most_purchases_using_functional_reference(groceries):
    customer, purchases = max(groceries.items(), key=get_total_purchase)
    return (customer, sum(purchases))


print(most_purchases_using_functional_reference(groceries))
