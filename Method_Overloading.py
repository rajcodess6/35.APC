class Shape:
    def area(self, a, b=0):
        if b == 0:
            print("Area of square:", a * a)
        else:
            print("Area of rectangle:", a * b)

s = Shape()
s.area(5)
s.area(5, 10)