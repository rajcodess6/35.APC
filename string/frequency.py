s = input("Enter string: ")
ch = input("Enter character: ")

count = 0

for x in s:
    if x == ch:
        count += 1

print("Frequency =", count)