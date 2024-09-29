class human():
    def __init__(self):
        self.num_eyes=2
        self.num_hands=2
    def eat(self):
        print("I can eat")
    def work(self):
        print("I can work")
class male(human):
    def __init__(self,name,heart):
        super().__init__()
        self.name=name
        self.heart=heart
    def work(self):
        print("I can play")
    def show(self):
        print("I can dance")
class boy(male):
    def __init__(self,age,name,heart):
        male.__init__(self,name,heart)
        self.age=age
    def work(self):
        print("I can see")
boy_1=boy(2,"lokesh",2)
print(boy_1.num_hands)

