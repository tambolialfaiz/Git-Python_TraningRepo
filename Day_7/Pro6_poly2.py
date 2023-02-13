# class Dog:
#     def __init__(self,str):
#         self.name=str
#     def hello(self):
#         print("Bhu Bhu")
#
# class Cat():
#     def __init__(self,str):
#         self.name=str
#     def hello(self):
#         print("Mau Mau")
#
# class Cow():
#     def __init__(self,str):
#         self.name=str
#     def hello(self):
#         print("Moo Moo")
#
#
# animals=[Dog("Doberman"),Cat("Tom"),Cow("Kapila")]
#
# for animal in animals:
#     animal.hello()
# #






class Employee():
    def __init__(self,str):
        self.EmpName=str

    def hello(self):
        print("We Are Employess")

class Father():
    def __init__(self,str):
        self.Name=str
    def hello(self):
        print("Father is a real hero")

class Brother():
    def __init__(self,str):
        self.name=str

    def hello(self):
        print("Big B is Huge Supporter")

man=[Employee("Alfaiz"),Father("Ejaj Tamboli"),Brother("Me Myself")]

for he in man:
    he.hello()


