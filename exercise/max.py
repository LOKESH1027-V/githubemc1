number=input("ENter the numbers separeatead by comma:")
list1=number.split(',')
list=[]
print(list1)
for i in list1:
    list.append(i)
l=len(list)  

for i in range(0,l):
    if i>i+1:
        max=i
        
    else:
        max=i    
print("THE MAX NUMBER IS ",list[max-1])        
