import random
import projectpy.Art.stages as stages
word=["apple","orange","mango"]
guess=random.choice(word)
print(guess)
display=[]
for i in guess:
    display.append("_")
print(display)    
game_over=False
lives=0
live=0
while not game_over or live <=6:
    guess_letter=input("Guess the letter:")
    for position in range(len(guess)):
        letter=guess[position]
        if letter==guess_letter:
            display[position]=letter
            print(display)
    if  guess_letter not in word:
        lives +=1
        print(stages.h[lives])
        if lives==6:
            print("You loss")
    if "_" not in display:
        print("You win")   
    live +=1
    
