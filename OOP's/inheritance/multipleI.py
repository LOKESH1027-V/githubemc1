class human():
    def __init__(self):
        self.num_eyes=2
        self.num_hands=2
    def eat(self):
        print("I can eat")
    def work(self):
        print("I can work")
class male():
    def __init__(self,language):
        self.language=language
    def work(self):
        print("I can code")
    def skill(self):
        print("I can surview")
class boy(human,male):
    def __init__(self,name,numheart,language):
        super().__init__()
        male.__init__(self,language)
        self.name=name
        self.num_heart=numheart
    def work(self):

        print("I can play")
    def dispalay(self):
        print(f"Hi,I am {boy_1.name} and I have {boy_1.num_heart} hearts .I am working in {boy_1.language} language")
boy_1=boy("lokesh",2,"python")
boy_1.dispalay()
print(boy.mro())