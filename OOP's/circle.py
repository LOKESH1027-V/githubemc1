class Circle:
    pi=3.14
    def __init__(self,radius):
        self.radius=radius
        self.area=Circle.pi*radius*radius
    def Circumference(self):
        return 2*Circle.pi*self.radius
Circle_1=Circle(4)
print(Circle_1.Circumference())