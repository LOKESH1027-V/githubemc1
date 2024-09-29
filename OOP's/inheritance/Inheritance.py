class human:
    def __init__(self,heart):
        self.num_eyes=2
        self.heart=heart
    def eat(self):
        print("I can eat")
    def play(self):
        print("I can play")
class male(human):
    def __init__(self,name,heart):
        super().__init__(heart)
        self.name=name

    def bark(self):
        super().eat()
        super().play()
        print("I can flirt")
male_1=male("loki",2)
male_1.bark()
print(male_1.num_eyes)
print(male_1.heart)