text = "968-Maria, ( D@t@ Engineer ) ;; 27y  "

text = text.strip() # strip the end white spaces
text = text.replace("@", "a").replace("(", "").replace(")","").replace(";;", ",") #replace unwanted characters
text = text[4:-1].lower() # slicing and lowercase the string
broken = text.split(",") #split into 3 parts using comma separator

name = broken[0] 
role = broken[1].strip()
age = broken[2].strip()

print(f"name: {name} | role: {role} | age: {age}")