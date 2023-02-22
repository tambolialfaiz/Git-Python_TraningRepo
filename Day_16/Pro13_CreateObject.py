class car:
    wheels=4

    def __init__(self,style,color):
        self.color=color
        self.style=style
    # def __str__(self):
    #     return f"Car name is {self.style} And My car color {self.color}"
obj=car("Audi","Black")
print(obj.color)
print(obj.style)

obj.style="Lambargini"
print(obj.style)

#In this example i understand which aregument you passed first in init method at the print of time they take it the first argument.