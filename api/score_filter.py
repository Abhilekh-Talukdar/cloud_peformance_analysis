"""Validation helpers for review-list query parameters."""

import math


def parse_score_filter(raw_value: str | None) -> float | None:
    """Parse an optional finite numeric score threshold.

    Returns None when the filter is absent. Raises ValueError for malformed
    or non-finite values so API views can return a client error instead of
    passing invalid values into the ORM.
    """
    if raw_value is None:
        return None

    try:
        score = float(raw_value)
    except (TypeError, ValueError) as error:
        raise ValueError("score must be a valid number.") from error

    if not math.isfinite(score):
        raise ValueError("score must be a finite number.")

    return score
