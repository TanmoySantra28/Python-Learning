#case conversion

text = "tanmoy SANTRA"

print(text.lower())
print(text.upper())

# clean data before matching
search = "Email ".upper().strip()
data = "emaIL".upper()

print(search == data)