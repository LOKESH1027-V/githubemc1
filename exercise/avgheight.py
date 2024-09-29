import random
height=(input("Enter the height of peoples separated by comma:"))
height=height.split(",")
a=0
j=0
for i in height:
    a +=int(height[0])
    j +=1

print(a)
print(j)
avg=a/j
print(f"Average height of the people are {round(avg)}")    


