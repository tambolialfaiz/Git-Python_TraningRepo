class bike:
    name=""
    gear=0

honda=bike()

honda.name="Mountain Bike"
honda.gear=5

print(f"I'm ride the {honda.name} they have {honda.gear}")



# ..............................Multiple objects of python classes..............

class Emoloyee:
    employeeId=0

employee1=Emoloyee()
employee2=Emoloyee()

employee1.employeeId=1051
print(f"Employee  id : {employee1.employeeId}")

employee2.employeeId=4586
print(f"Employee id : {employee2.employeeId}")