import os

TEXT = """Every entry tonight asked you for something. This one asks nothing. Past the screen, rain is falling on a tin roof, slow and even, and nobody counts the drops. They fall. They land. They are enough. The next word will still be there when you are ready, in no hurry at all.
"""

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(TEXT)
