class student:
    def __init__(self):
        self._name=""

    def getname(self):
        return self._name
    def setname(self,name):
        self._name=name

obj=student()
obj.setname("Full Stack Devloper")
name=obj.getname()
print(name)