class Grandfather:
    def house(self):
        print("Grandfather has a house")

class Father(Grandfather):
    pass

class Son(Father):
    pass

s = Son()
s.house()