# class A:
#     def displayA(self):
#         print("Hello Alfaiz")
# class B(A):
#     def displayB(self):
#         print("Hii Shubhangi")
# obj=B()
# obj.displayA()
# obj.displayB()




# ........................multipal inheritance................

class Hii:
    def func1(self):
        print("good morning ")
class Hello:
    def func2(self):
      print("Good Afternoon")
class Hey(Hii,Hello):
    def func3(self):
        print("I love  Myself ")

obj=Hey()
obj.func1()
obj.func2()
obj.func3()
