class Person:
    def show(self):
        print("I am a person")

class Student(Person):
    pass

class Sports(Person):
    pass

class Player(Student, Sports):
    pass

p = Player()
p.show()