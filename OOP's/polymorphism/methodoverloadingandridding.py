#Method overloading
class demo():
    def add(*args):
        total=0
        for i in args:
            total=i+total
        return total
#print(demo.add(1,23,4))
#print(demo.add(12,3,4,2,2,))
#method overriding
class stu:
    def sleep(self):
        print("I can sleep")
    def study(self):
        print("I can study")
class s1(stu):
    def sleep(self):
        print("I can")
        super().sleep()
c=s1()
c.sleep()
