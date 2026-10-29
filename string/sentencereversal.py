s = input("Enter sentence: ")

words = s.split()
result = ""

for word in reversed(words):
    result += word + " "

print(result)