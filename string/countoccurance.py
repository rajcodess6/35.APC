s = input("Enter sentence: ")
word = input("Enter word: ")

words = s.split()
count = 0

for w in words:
    if w == word:
        count += 1

print("Occurrences =", count)