class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Constructor called")

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

    def __del__(self):
        print("Destructor called")

s1 = Student("Shreeja", 20)
s2 = Student("Brahmee",22)
s3 = Student("samiksha",19)

s1.display()
s2.display()
s3.display()

del s1
del s2
del s3