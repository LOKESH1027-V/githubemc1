#sorting hat
gryffindor=0
hufflepuff=0
ravenclaw=0
slytherin=0
 
print('Q1)Do you like Dawn or Dusk?')
print('1)Dawn')
print('2)Dusk')
answer=int(input('enter 1 or 2'))
if answer==1:
    gryffindor+=1
    ravenclaw+=1
elif answer==2:
    hufflepuff+=1
    slytherin+=1
else:
    print('not for anyone')
print("Q2) When I’m dead, I want people to remember me as:")
print("    1) The Good")
print("    2) The Great")
print("    3) The Wise")
print("    4) The Bold")
answer=int(input("enter number"))
if answer==1:
    hufflepuff+=2
elif answer==2:
    slytherin+=2
elif answer==3:
    ravenclaw+=2
elif answer==4:
    gryffindor+=2

most_points=max(gryffindor, ravenclaw, hufflepuff, slytherin)
                
if gryffindor == most_points:
  print('🦁 Gryffindor!')
elif ravenclaw == most_points:
  print('🦅 Ravenclaw!')
elif hufflepuff == most_points:
  print('🦡 Hufflepuff!')
else:
  print('🐍 Slytherin!')             


           