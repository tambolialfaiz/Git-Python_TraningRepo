class Vehile:

    color="Black"

    def __init__(self,name,top_speed,mileage):
        self.top_speed=top_speed
        self.name=name
        self.mileage=mileage

class TransportVehicle(Vehile):
    pass
class Car(Vehile):
    pass

Bus=TransportVehicle("Bolero",120,45)
print(Bus.color,Bus.name,"Top Speed",Bus.top_speed,"Mileage:",Bus.mileage)

car=Car("Ferrari",250,60)
print(car.color,car.name,"Top Speed",car.top_speed,"Mileage:",car.mileage)