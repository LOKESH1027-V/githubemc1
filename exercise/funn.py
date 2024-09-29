n=int(input())
b=list(bin(n)) 
d=[]
for i in range(2,len(b)):
    d.append(b[i])    
c=[]
for i in range(len(b),2,-1):
    c.append(b[i-1])
print(c)
if d==c:
    print("yes")
else:
    print("no")        