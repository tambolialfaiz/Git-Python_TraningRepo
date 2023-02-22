# Create a child class Bus that will inherit all of the variables and methods of the Vehicle class

class vehicle:
     def __init__(self,name,maxspeed,avarage):
         self.name=name
         self.maxspeed=maxspeed
         self.avarage=avarage

class Car(vehicle):
    pass

Audi_car=Car("Audi-AQ3",250,50)
print(f"My Car Name is {Audi_car.name} and the top speed of my car is {Audi_car.maxspeed} also they have give me {Audi_car.avarage} Avarage.")