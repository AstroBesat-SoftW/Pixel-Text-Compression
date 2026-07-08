"""
Stage 2 — Run-Length Encoding (illustrative snippet)
------------------------------------------------------
Simplified excerpt showing the CONCEPT of the custom RLE pass:
collapsing consecutive repeated values into "count + value" pairs.

This is NOT the full pipeline (integration with the range-compressed
matrix and the alphanumeric mapping stage has been omitted).
See the whitepaper in /docs for the complete methodology.
"""

def rle_concept(values):
    """
    Given a list of small integers (already range-compressed to 0-25),
    collapse consecutive repeats into (count, value) pairs.

    Example:
        input:  [17, 17, 17, 17, 17]
        output: [(5, 17)]
    """
    if not values:
        return []

    result = []
    current = values[0]
    count = 1

    for v in values[1:]:
        if v == current:
            count += 1
        else:
            result.append((count, current))
            current = v
            count = 1
    result.append((count, current))
    return result

# --- conceptual usage ---
# compressed_row = rle_concept(range_compressed_row)
# # (count, value) pairs are then passed to the alphanumeric mapping stage
