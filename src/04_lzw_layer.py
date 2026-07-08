"""
Stage 4 — Dictionary-based Compression (illustrative snippet)
-----------------------------------------------------------------
Simplified excerpt showing the general CONCEPT of an LZW-style pass:
learning repeated substrings and re-encoding them as single Unicode
symbols outside the normal ASCII range.

This is a conceptual sketch only — the actual dictionary bootstrapping,
code-width handling, and file encoding used in the real pipeline have
been intentionally left out. See the whitepaper in /docs for the full
methodology and worked examples (e.g. "4M3Z" -> single symbol).
"""

def build_seed_dictionary():
    """Seed dictionary: every single character maps to itself initially."""
    return {chr(i): i for i in range(256)}

def concept_pass(text):
    """
    Sketch of the learning loop: walk through the text, and whenever a
    new (already-seen-prefix + next-char) combination appears, register
    it as a new dictionary entry mapped to the next available code.
    Full implementation, code emission, and reverse-lookup handling
    are omitted here — see whitepaper for details.
    """
    dictionary = build_seed_dictionary()
    next_code = 256
    current = ""
    codes = []

    for ch in text:
        combined = current + ch
        if combined in dictionary:
            current = combined
        else:
            codes.append(dictionary[current])
            dictionary[combined] = next_code
            next_code += 1
            current = ch
    if current:
        codes.append(dictionary[current])

    return codes  # in the real pipeline these codes become Unicode symbols
