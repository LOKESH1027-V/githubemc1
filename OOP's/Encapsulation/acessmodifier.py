class student():
    def __init__(self,name,rollno,age):
        self.name=name
        self._rollno=rollno
        self.__age=age
    def display(self):
        print(f"Hi hello {self.name} and my rollno is {self._rollno}. My age is {self.__age}")
    def get_age(self):
        return self.__age
    def set_age(self,age):
        self.__age=age
class stu(student):
    pass
s1=student("loki",18,18)
print(s1._student__age)
print(s1.get_age())
s1.set_age(20)
print(s1._student__age)
print(dir(s1._student__age))