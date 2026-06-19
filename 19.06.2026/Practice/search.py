#search

#check country code
phone = "+91 82403 21541"
print(phone.startswith("+91"))
print(phone.startswith("+49"))

#check domain of an email
email = "tanmoy@gmail.com"
print(email.endswith("gmail.com"))
print(email.endswith("outlook.com"))

#check for @ in an email
print("@" in email)
print("$" in email)

#check if an url is an api endpoint
url = "https://api.company.com/v1/data"
print("/api" in url)