class bill():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __gt__(self, other):
        if self.age>other.age:
            return True
        else:
            return False
c1=bill("loki",19)
c2=bill("thokesh",20)
if c1>c2:
    print(f"{c1.name} is going to pay the bill")
else:
    print(f"{c2.name} is going to pay the bill")
#int.__add__()