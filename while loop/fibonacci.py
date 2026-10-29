n = int(input("Enter n: "))

a = 0
b = 1

while a <= n:
    print(a, end=" ")
    c = a + b
    a = b
    b = c