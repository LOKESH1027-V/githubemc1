class duck:
    def swim(self):
        print("I can swim")
    def speak(self):
        print("I can speak")
class dog:
    def swim(self):
        print("I can swim")
    def speak(self):
        print("I can speak")
class person:
    def speak(self):
        print("HI")
class display:

 def display(duck):
    duck.swim()
    duck.swim()
d=duck()
display.display(d)
c=dog()
display.display(c)
p=person()
display.display(p)

