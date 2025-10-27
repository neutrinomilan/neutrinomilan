import random
import re
from pathlib import Path

# Base directory of this script
base = Path(__file__).resolve().parent

quotes_path = base / "quotes.txt"
readme_path = base / "README.md"

# Read quotes
with open(quotes_path, "r", encoding="utf-8") as f:
    quotes = [line.strip() for line in f if line.strip()]

if not quotes:
    raise ValueError("No quotes found in quotes.txt")

quote = random.choice(quotes)

# Read README
with open(readme_path, "r", encoding="utf-8") as f:
    readme = f.read()

# Replace between markers
updated = re.sub(
    r"<!--START_QUOTE-->.*?<!--END_QUOTE-->",
    f"<!--START_QUOTE-->\n> \"{quote}\" 💬\n<!--END_QUOTE-->",
    readme,
    flags=re.DOTALL
)

# Write back
with open(readme_path, "w", encoding="utf-8") as f:
    f.write(updated)

print(f"✅ Updated README.md with new quote: {quote}")
