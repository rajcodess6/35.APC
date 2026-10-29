s = input("Enter string: ")

rev = ""
for ch in s:
    rev = ch + rev

print("Reverse =", rev)