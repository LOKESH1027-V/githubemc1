import random
import projectpy.Art.stages as stages
list=["apple","orange","mango"]
choose=random.choice(list)
print(choose)
display=[]
for i in choose:
    display.append("_")
print(display)
game_over=False
live=-1
while not game_over:
    guess=input("Guess the word:")
    for position in range(len(choose)):   
        letter=guess[position] 
        if letter==choose:
            display[position]=letter
            print(display)
    if guess not in choose:
        live+=1
        print(stages.h[live])
        if live==0:
            print("you loose")
    if "_" not in display:
        print("you win")        
print(stages.h[live])        
