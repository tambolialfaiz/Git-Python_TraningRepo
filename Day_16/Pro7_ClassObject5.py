
class Dog:
	animal = 'dog'
	def __init__(self, breed):
		self.breed = breed
	def setColor(self, color):
		self.color = color
	def getColor(self):
		return self.color
Rodger = Dog("pug")
Rodger.setColor("brown")
print(Rodger.getColor())




class Car:
    CarName="Audi"
    def __init__(self,model):
        self.Model=model
    def setColor(self,color,model):
        self.Color=color
        self.Model=model
    def getColor(self):
        return self.Color,self.Model

Four=Car("A1")
Four.setColor("White","AQ")
print(Four.getColor())

