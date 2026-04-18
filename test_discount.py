import unittest
from discount import calculate_discounted_price

class TestDiscountCalculator(unittest.TestCase):

    def test_normal_discount(self):
        """Обычная скидка 20% на цену 1000"""
        self.assertEqual(calculate_discounted_price(1000, 20), 800.0)

    def test_zero_discount(self):
        """Скидка 0% - цена не меняется"""
        self.assertEqual(calculate_discounted_price(500, 0), 500.0)

    def test_full_discount(self):
        """Скидка 100% - итоговая цена 0"""
        self.assertEqual(calculate_discounted_price(250.5, 100), 0.0)

    def test_decimal_price(self):
        """Цена с десятичными долями и нецелая скидка"""
        self.assertEqual(calculate_discounted_price(99.99, 15), 84.99)

    def test_negative_price_raises_error(self):
        """Отрицательная цена вызывает исключение"""
        with self.assertRaises(ValueError):
            calculate_discounted_price(-100, 10)

    def test_discount_above_100_raises_error(self):
        """Скидка > 100% вызывает исключение"""
        with self.assertRaises(ValueError):
            calculate_discounted_price(200, 150)

    def test_negative_discount_raises_error(self):
        """Отрицательная скидка вызывает исключение"""
        with self.assertRaises(ValueError):
            calculate_discounted_price(200, -10)

if __name__ == "__main__":
    unittest.main(Добавлены unit-тесты)
