from abstraction_1 import vehicle
class scooty(vehicle):
    def __init__(self,n,color):
        super().__init__(n)
        self.color=color
    def start(self):
        print('Scooty is start by self')
    def display(self):
        print(f"My scooty color is {self.color}")
class bike(vehicle):
    def __init__(self,color,n):
        vehicle.__init__(self,n)
        self.color = color
    def start(self):
        print('Scooty is start by kick')

    def display(self):
        print(f"My scooty color is {self.color}")
class car(vehicle):
    def __init__(self,color,n):
        super().__init__(n)
        self.color = color

    def start(self):
        print('Scooty is start by key')

    def display(self):
        print(f"My scooty color is {self.color}")

