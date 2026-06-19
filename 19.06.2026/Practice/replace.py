# replace() method

#change date format
date = "12/01/2025"
print(date.replace("/","-"))

#change numeric format
num = "1234,67"
print(num.replace(",","."))

#change phone number format
ph_no = "567-3589-3345"
print(ph_no.replace("-","/"))

#remove any unwanted value
currency = "$98,125.80"
print(currency.replace("$","").replace(",","")) #chained methods