s = input("Enter string: ")

for ch in s:
    if s.count(ch) > 1:
        print(ch)