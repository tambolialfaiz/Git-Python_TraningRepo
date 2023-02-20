fun=(lambda a,b:a+b)(5,10)
print(fun)


# .....................................Class Object............................

class Myclass:
    x=5
obj=Myclass()
print(obj.x)


class pro:
    def __init__(self,name,age):
        self.EmpName=name
        self.EmpAge=age

obj=pro("Alfaiz",22)
print(obj.EmpName)
print(obj.EmpAge)



# .......................................Str Function......................

class Person:
    def __init__(self,name,mobNo,id):
        self.EmpName=name
        self.mobNo=mobNo
        self.id=id
    def __str__(self):
        return f"{self.EmpName} {self.mobNo} {self.id}"

obj=Person("Alfaiz",8956222832,150)

print(obj)