email = "esther@gmail.com"
#email cleaning
email = email.strip()
if email == "":
    print("email is empty")
#email.contains "@" and "."
elif not("." in email and "@" in email):
    print("email must contain @ and .")
elif email.count("@") != 1:
    print("email must contain only one @")
elif not email.endswith((".com", ".org", ".net")):
    print("must end with .com, org, or net")
elif len(email) > 254:
    print("email must be less than 254 characters")
elif not email[0]. isalnum() and email[-1]. isalnum():
    print("email must start and end with a letter or number")
else: 
    print("email is valid")
