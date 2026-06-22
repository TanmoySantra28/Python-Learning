import math as m

price = 35.536718

print(round(price))  # rounding to nearest whole number
print(round(price, 2))

print(m.floor(price))  # round down to floor

print(m.ceil(price))    # round up to ceiling

#cuts off the decimal part
print(m.trunc(price))
print(int(price))