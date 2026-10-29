class Person:
    def name(self):
        print("My name is Rahul")

class Student(Person):
    pass

class Teacher(Person):
    pass

s = Student()
t = Teacher()

s.name()
t.name()