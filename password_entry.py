password = input("What is the password? ")

min_length = 3
password_length = len(password)

while password_length < min_length:
    print("Invalid")
    password = input(">")
    password_length = len(password)
else:
    print("*" * password_length)
