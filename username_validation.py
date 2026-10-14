
username = input("Enter username: ")

if username.strip() == "":
    print("Invalid username: Username must not contain only spaces.")
elif len(username) < 5:
    print("Invalid username: Must contain at least 5 characters.")
elif username.lower() == "admin":
    print("Invalid username: Username cannot be 'admin'.")
else:
    print("Valid username.")
