password = input("Enter password: ")

upper = lower = digit = special = False

if len(password) < 8:
    print("Password must be at least 8 characters long")
else:
    for ch in password:
        if ch.isupper():
            upper = True
        elif ch.islower():
            lower = True
        elif ch.isdigit():
            digit = True
        elif ch != " ":
            special = True

    if upper and lower and digit and special:
        print("Valid Password")
    else:
        print("Invalid Password")
