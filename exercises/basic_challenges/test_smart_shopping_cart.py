import unittest

from smart_shopping_cart_challenge import generate_receipt


class TestGenerateReceipt(unittest.TestCase):

    def test_receipt_without_discount(self):
        cart = [
            ("Apple", 1.5, 10),  # $15.00
            ("Banana", 0.75, 20),  # $15.00
            ("Chocolate", 2.0, 5),  # $10.00
        ]
        result = generate_receipt(cart)
        self.assertIn("Subtotal: $40.00", result)
        self.assertIn("(No discount applied)", result)

    def test_receipt_with_discount(self):
        cart = [
            ("Laptop Bag", 45.0, 1),  # $45.00
            ("Wireless Mouse", 25.0, 2),  # $50.00
            ("Notebook", 12.5, 3),  # $37.50
        ]
        result = generate_receipt(cart)
        self.assertIn("Subtotal: $132.50", result)
        self.assertIn("Discount Applied: 10% (-$13.25)", result)
        self.assertIn("Total after discount: $119.25", result)

    def test_empty_cart(self):
        cart = []
        result = generate_receipt(cart)
        self.assertIn("Subtotal: $0.00", result)
        self.assertIn("(No discount applied)", result)


if __name__ == "__main__":
    unittest.main()
