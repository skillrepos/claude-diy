"""Command-line checkout for the Lantern Lane Books web shop.

Usage:  python3 checkout.py <subtotal> [coupon-code]
Example: python3 checkout.py 80 SAVE-15
"""
import sys

from pricing import order_total


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print("Usage: python3 checkout.py <subtotal> [coupon-code]")
        return 2
    subtotal = float(argv[1])
    coupon = argv[2] if len(argv) > 2 else ""
    total = order_total(subtotal, coupon)
    print(f"Total to pay: ${total:.2f}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
