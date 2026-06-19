# detect how many white spaces are there

text = "  Tanmoy   "

print(len(text))
print(len(text.strip()))

print(f"Difference = {len(text) - len(text.strip())}")
print(f"Is my data clean? {len(text) == len(text.strip())}")
