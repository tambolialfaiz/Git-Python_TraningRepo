class Car:
    wheels = 4
    def __init__(self, color, style):
        self.color = color
        self.style = style
    def Data(self):
        print("This car is a", self.color, self.style)
    def changeColor(self, color):
        self.color = color
c = Car('Black', 'Rolls Royles')
c.Data()
c.changeColor('White')
c.Data()
