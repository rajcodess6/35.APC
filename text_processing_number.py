text = input("Enter phone number: ")

if len(text) == 10 and text.isdigit():
    print("Valid phone number")
else:
    print("Invalid phone number")