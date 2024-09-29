import random
import os
import Art.logo as logo
import Dataset.hi as hi
print(logo.higher_lower)
def show(number):
 name=number["name"]
 country=number["country"]
 social=number["socialmedia"]
 return f"{name} ,{social}  , {country}"
def check(guess,salary1,salary2):
  if salary1>salary2:
     if guess==1:
       return True
     else:
       return False
  else:
    if guess==2:
       return True
    else:
       return False
score=0    
flag=True
two=random.choice(hi.list)
while flag:
 one=two
 two=random.choice(hi.list)
 while one==two:
   two=random.choice(hi.list)
 print(f"Compare 1 :{show(one)}")
 print(logo.vs)
 print()
 print(f"Compare 2 :{show(two)}")
 guess=int(input("Who has more salary?.Type 1 or 2:"))
 salary1=one["salary"]
 salary2=two["salary"]
 ans=check(guess,salary1,salary2)
 os.system('cls')
 print(logo.higher_lower)
 if ans==True:
   score+=1
   print(f"Your are right.. Your  score is {score}")
 else:
   print(f"You are wrong.... Your final score is {score}") 
   flag=False

   
 
 
   

