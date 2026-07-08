"""
Stage 3 — Alphanumeric Mapping (illustrative snippet)
--------------------------------------------------------
Simplified excerpt showing the CONCEPT of mapping small integers (0-25)
onto single letters (A-Z) to shrink two-digit numbers into one character.

This is NOT the full pipeline (full row assembly and file writing have
been omitted). See the whitepaper in /docs for the complete methodology.
"""

def value_to_letter(value):
    """Map a 0-25 integer to a single uppercase letter (A-Z)."""
    value = max(0, min(25, value))
    return chr(65 + value)

def letter_to_value(letter):
    """Reverse of value_to_letter."""
    return ord(letter.upper()) - 65

# --- conceptual usage ---
# for count, value in rle_pairs:
#     letter = value_to_letter(value)
#     token = f"{count}{letter}" if count > 1 else letter
#     # tokens are concatenated per row, then passed to the
#     # dictionary-based compression stage (Stage 4)
