# class object with method

class home:
    def __init__(self,width,leanth):
        self.HomeWidth=width
        self.HomeLeanth=leanth
    def Area(self):
        return self.HomeWidth*self.HomeLeanth

w=50
l=10

size=home(w,l)
print("Total Area of House is :",size.Area())

# ..............................Pro1......................................
class AdmissionForm:
    def __init__(self,name,course):
        self.name =name
        self.course=course
    def __repr__(self):
        return repr("Name is"+" "+self.name+"  "+"course"+" "+self.course)
applicant = AdmissionForm("Alfaiz","Full Stack devloper")

print(applicant)
repr(applicant)

# ..................................Pro2..................................

# create a class
class Room:
    length = 0.0
    breadth = 0.0
    def calculate_area(self):
        print("Area of Room =", self.length * self.breadth)
study_room = Room()
study_room.length = 42.5
study_room.breadth = 30.8
study_room.calculate_area()