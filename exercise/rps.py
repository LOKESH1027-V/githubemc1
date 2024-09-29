import random
print("0 for Rock")
print("1 for Paper \n2 for scissors")
game=['Rock','Paper','sicessors']
u=int(input("Enter your choice:"))
c=random.randint(0,2)
print("Your choice is     :",game[u])
print("Computer choice is :",game[c])
if c==u:
    print("Tie")
elif ((c==0 and u==2)  ):
      print("You loss")
elif u==0 and c==2:
     print("You win")
elif c>u:
    print("You loss")
else:
     print("you win")                 