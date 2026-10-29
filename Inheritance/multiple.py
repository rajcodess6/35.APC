class Father:
    def skills1(self):
        print("Driving")

class Mother:
    def skills2(self):
        print("Cooking")

class Child(Father, Mother):
    pass

c = Child()
c.skills1()
c.skills2()