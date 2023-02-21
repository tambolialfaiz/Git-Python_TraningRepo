
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        print("Hi, my name is", self.name, "and I'm", self.age, "years old.")
person1 = Person("Alfaiz", 22)
person1.introduce()
