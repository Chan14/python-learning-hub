import unittest

from numbers_and_strings_challenges import convert_temperature_functional


class TestTemperatureConversion(unittest.TestCase):
    def test_celsius_to_farenheit(self):
        result = convert_temperature_functional(0, "C")
        self.assertEqual(result, "0°C is 32.0°F")

        result = convert_temperature_functional(100, "C")
        self.assertEqual(result, "100°C is 212.0°F")

        result = convert_temperature_functional(37, "C")
        self.assertEqual(result, "37°C is 98.6°F")

    def test_fahrenheit_to_celsius(self):
        result = convert_temperature_functional(32, "F")
        self.assertEqual(result, "32°F is 0.0°C")

        result = convert_temperature_functional(212, "F")
        self.assertEqual(result, "212°F is 100.0°C")

        result = convert_temperature_functional(98.6, "F")
        self.assertEqual(result, "98.6°F is 37.0°C")

    def test_invalid_scale(self):
        with self.assertRaises(ValueError):
            convert_temperature_functional(100, "K")


if __name__ == "__main__":
    unittest.main()
