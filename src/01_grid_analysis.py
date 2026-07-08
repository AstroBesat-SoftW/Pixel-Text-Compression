"""
Stage 1 — Grid Averaging (illustrative snippet)
-------------------------------------------------
This is a simplified excerpt showing the CONCEPT behind Stage 1:
splitting an image into a grid and reducing each block to a single
average grayscale value.

This is NOT the full pipeline (grid-size handling, edge-case cropping,
range compression, and output formatting have been omitted on purpose).
See the whitepaper in /docs for the complete methodology.
"""

from PIL import Image, ImageStat

def average_block_value(image, box):
    """Return the average grayscale value (0-255) of a cropped region."""
    block = image.crop(box).convert("L")
    stat = ImageStat.Stat(block)
    return int(round(stat.mean[0])) if stat.mean else 0

# --- conceptual usage ---
# img = Image.open("input.jpg")
# for each grid cell (row, col):
#     box = (...)  # coordinates omitted
#     value = average_block_value(img, box)
#     # value gets appended to a row matrix, then range-compressed
#     # (see whitepaper, Stage 1 -> Stage 1.5)
