import math
can=7
height=int(input("Enter height:"))
width=int(input("Enter width:"))
c=(height*width)/7
n=math.ceil(c)
print(f"You need {n} cans of paint")