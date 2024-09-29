#def add(a,b):
#    print(f"Sum is {a+b}" )
#add(10,27)
'''    
def v(name,subject,dep="agri"):
    print(f"hi {name}")
    print(f"do you teach {subject}")
    print(f"are you from {dep} depaartment")
v("lokesh","agri")#default and positonal arguments
v("loki",subject="agri",dep="mech")#keyword argument with default    
'''
def add(*numbers):#It storre the vaule in tuple[]
    a=0
    for i in numbers:
        a=a+i
    print(a)    
add(27,10)    
add(1,2,3,4,5,6,7,89) 