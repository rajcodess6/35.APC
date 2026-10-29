s = input("Enter string: ")

freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

values = sorted(freq.values(), reverse=True)

second = values[1]

for ch in freq:
    if freq[ch] == second:
        print("Second most frequent =", ch)
        break