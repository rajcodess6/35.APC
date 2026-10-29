p = input("Enter password: ")

upper = lower = digit = special = 0

for ch in p:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
    elif ch.isdigit():
        digit += 1
    else:
        special += 1

if len(p) >= 8 and upper > 0 and lower > 0 and digit > 0 and special > 0:
    print("Valid Password")
else:
    print("Invalid Password")