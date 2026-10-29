s = input("Enter string: ")

result = ""

for ch in s:
    if ch != " ":
        result += ch

print(result)