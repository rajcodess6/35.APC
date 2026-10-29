s = input("Enter sentence: ")

words = s.split()
result = ""

for word in words:
    result += word[0].upper() + word[1:] + " "

print(result)