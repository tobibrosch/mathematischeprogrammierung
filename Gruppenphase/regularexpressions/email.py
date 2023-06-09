import re

email = input("Whats your email?").strip().lower()

if re.search(r"^\w+\.?\w+@(\w+\.)?\w+\.(de|com|us|edu)$",email):
    print("valid")
else:
    print("not valid")

url = input("URL: ").strip()

name = re.search(r"^https?://twitter\.com/(?:(\w/)*)(\w+/?)",url).group(1)   


print(name)