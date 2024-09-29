import os
print(".................................<WELCOME TO THE AUCTION PROGRAM>..........................................")

def dev(d):
    high=0
    for i in d:
        price=d[i]
        if price>high:
            high=price
            win=i
    print(f"winner is {win} with the bit price {high}")        
state=True
d={}
while  state:
    name=input("What is your name:")
    bit=int(input("Enter your bit ammount:"))
    d[name]=bit
    n=input("Are there any other bitter:").lower()
    if n=="no":
        os.system('cls')
        state=False
    elif n=="yes":
        os.system('cls')    
de=dev(d)        



                    