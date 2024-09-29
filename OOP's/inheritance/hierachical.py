class parent():
    def __init__(self):
        self.num_eyes=3
        self.num_hands=4
    def eat(self):
        print("I can eat")
class child_1(parent):
    def __init__(self):
     parent.__init__(self)
    def work(self):
        print("I can work")
class child_2(parent):
    def __init__(self):
        super().__init__()
    def work(self):
        print("I can work hard")
boy=child_2()
print(boy.num_hands)