"""Pricing rules for the Lantern Lane Books web shop (a made-up store)."""

SHIPPING_FEE = 5.00
FREE_SHIPPING_OVER = 50.00
MAX_DISCOUNT_PERCENT = 50


def normalize_code(code: str) -> str:
    """Trim spaces and upper-case a coupon code."""
    return code.strip().upper()


def coupon_percent(code: str) -> int:
    """Return the discount in a code like 'SAVE-15' (15 percent off)."""
    return int(code.split("-")[1])


def order_total(subtotal: float, coupon_code: str) -> float:
    """Return what the customer pays: subtotal, minus any coupon, plus shipping."""
    code = normalize_code(coupon_code)
    percent = min(coupon_percent(code), MAX_DISCOUNT_PERCENT)
    discounted = subtotal * (100 - percent) / 100
    shipping = 0.0 if discounted >= FREE_SHIPPING_OVER else SHIPPING_FEE
    return round(discounted + shipping, 2)
