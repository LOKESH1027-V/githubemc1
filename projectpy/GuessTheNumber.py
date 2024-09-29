import random
import Art.logo as logo
n=random.randint(1,20)
def easy():
    life!=10
    print("You have 10 lifes:")
    print("You must have to guess the number correctly with in 10 cahnces:")
    while life:
        number=int(input("Make a Guess:"))
        if number==n:
            print("YOU WON")
            break
        elif number<n:
            print("Your guess is low:")
            life=life-1
        else:
            print("your guess is high:")
            life=life-1   
        print(f"You have {life} chances left") 
    if life==0:      
     print("BETTER LUCK NEXT TIME.")
def hard():
    life=5
    print("You have 5 lifes:")
    print("You must have to guess the number correctly with in 5 cahnces:")
    life=5
    while life!=0:
        number=int(input("Make a Guess:"))
        if number==n:
            print("YOU WON")
            break
        elif number<n:
            print("Your guess is low:")
            life=life-1
        else:
            life=life-1
            print("your guess is high:")
        print(f"You have {life} chances left") 
    if life==0:       
     print("BETTER LUCK NEXT TIME.")     
def display():
    print(logo.logo)
    print("Let me think of a number between 1 to 50:")
    stage=input("Do you want to the game to be easy or hard:").lower()
    if stage=="easy":
        easy()
    elif stage=="hard":
        hard()
display()        

