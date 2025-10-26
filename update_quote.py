import random

# Read quotes
with open("quotes.txt", "r", encoding="utf-8") as f:
    quotes = [line.strip() for line in f if line.strip()]

quote = random.choice(quotes)

# Read README
with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

# Replace between markers
import re
updated = re.sub(
    r"<!--START_QUOTE-->.*?<!--END_QUOTE-->",
    f"<!--START_QUOTE-->\n> \"{quote}\" 💬\n<!--END_QUOTE-->",
    readme,
    flags=re.DOTALL
)

# Write back
with open("README.md", "w", encoding="utf-8") as f:
    f.write(updated)
