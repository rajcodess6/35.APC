story = input("Enter your story: ")
stripped = [s.strip() for s in story.split(".")]
lines = [s for s in stripped if s]
total = 0
not_t = 0
for line in lines:
    total += 1
    if line[0] != "T":
        not_t += 1

print("Total lines:", total)
print("Not starting with T:", not_t)