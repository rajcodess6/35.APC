s = input("Enter string: ")

for ch in s:
    if s.index(ch) == s.find(ch):
        print(ch, "=", s.count(ch))