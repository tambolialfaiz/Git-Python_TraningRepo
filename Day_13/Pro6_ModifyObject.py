class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)
    print("My age is " + str(self.age))

obj = Person("Alfaiz", 36)
obj.age=22
obj.myfunc()