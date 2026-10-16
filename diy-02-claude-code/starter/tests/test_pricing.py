import unittest

from pricing import coupon_percent, normalize_code, order_total


class PricingTests(unittest.TestCase):
    def test_coupon_percent_reads_the_number(self):
        self.assertEqual(coupon_percent("SAVE-20"), 20)

    def test_codes_are_trimmed_and_upper_cased(self):
        self.assertEqual(normalize_code("  save-10 "), "SAVE-10")

    def test_coupon_takes_percent_off(self):
        self.assertEqual(order_total(100.00, "SAVE-15"), 85.00)

    def test_discount_is_capped(self):
        self.assertEqual(order_total(200.00, "SAVE-80"), 100.00)

    def test_shipping_added_on_small_orders(self):
        self.assertEqual(order_total(30.00, "SAVE-10"), 32.00)

    def test_free_shipping_on_large_orders(self):
        self.assertEqual(order_total(60.00, "SAVE-10"), 54.00)


if __name__ == "__main__":
    unittest.main()
