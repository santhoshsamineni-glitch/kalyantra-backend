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
def merge_intervals(intervals: List[Interval]) -> List[Interval]:
    """
    Merges overlapping OR touching half-open intervals.
    Returns a sorted list of merged intervals.
    """

    if not intervals:
        return []

    # Validate all intervals first
    for interval in intervals:
        validate_interval(interval)

    # Sort intervals by start value
    sorted_intervals = sorted(intervals, key=lambda x: x[0])

    merged = [sorted_intervals[0]]

    for current in sorted_intervals[1:]:
        last_start, last_end = merged[-1]
        current_start, current_end = current

        # If overlapping or touching
        if current_start <= last_end:
            # Merge
            merged[-1] = (
                last_start,
                max(last_end, current_end)
            )
        else:
            merged.append(current)

    return merged
def subtract_multiple(base: Interval, blocks: List[Interval]) -> List[Interval]:
    """
    Subtracts multiple intervals (blocks) from a base interval.
    Returns remaining intervals after subtraction.
    """

    validate_interval(base)

    if not blocks:
        return [base]

    # Validate and trim blocks to base boundaries
    trimmed_blocks = []
    base_start, base_end = base

    for block in blocks:
        validate_interval(block)
        block_start, block_end = block

        # Ignore completely outside blocks
        if block_end <= base_start or block_start >= base_end:
            continue

        # Trim to base boundaries
        trimmed_start = max(block_start, base_start)
        trimmed_end = min(block_end, base_end)

        if trimmed_start < trimmed_end:
            trimmed_blocks.append((trimmed_start, trimmed_end))

    if not trimmed_blocks:
        return [base]

    # Merge overlapping or touching blocks
    merged_blocks = merge_intervals(trimmed_blocks)

    remaining = []
    current_start = base_start

    for block_start, block_end in merged_blocks:
        if current_start < block_start:
            remaining.append((current_start, block_start))

        current_start = block_end

    # Add last segment if any remains
    if current_start < base_end:
        remaining.append((current_start, base_end))

    return remaining
