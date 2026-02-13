from decimal import Decimal
from typing import Tuple

Interval = Tuple[Decimal, Decimal]

def validate_interval(interval: Interval) -> None:
    """
    Validates that an interval:
    - contains Decimal values
    - start < end (half-open rule)
    - no negative values
    """

    start, end = interval

    if not isinstance(start, Decimal) or not isinstance(end, Decimal):
        raise TypeError("Interval values must be Decimal.")

    if start < Decimal("0") or end < Decimal("0"):
        raise ValueError("Chainage cannot be negative.")

    if start >= end:
        raise ValueError("Invalid interval: start must be less than end.")
