His=input("Enter your name:")
Her=input("Enter Her name:")
His=His.lower()
Her=Her.lower()
t=His.count("t")+Her.count("t")
r=His.count("r")+Her.count("r")
u=His.count("u")+Her.count("u")
e=His.count("e")+Her.count("e")
l=His.count("l")+Her.count("l")
o=His.count("o")+Her.count("o")
v=His.count("v")+Her.count("v")
e=His.count("e")+Her.count("e")
t=t+r+u+e
t=str(t)
l=l+o+v+e
l=str(l)
p=t+l
per=int(p)
if per>=10 or per>90:
    print('YOU WILL ALWAYS TOGETHER')
    print("Your score is ",per)
elif 40<per>50:
    print("She will always be on your side")
else:
    print(f"Your score is {per}")        