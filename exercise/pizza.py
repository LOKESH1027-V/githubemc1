size=input("Enter what size pizza do you want L/M/S")
if size=='S' or size=='s':
    bill=100
    
elif size=='M' or size=='m':
        bill=200      
else:
      bill=300
      
peporoni=input("do you want peporanines?")   
if peporoni=='yes':
      if size=='S' or size=='s':
         bill+=10
        
      elif size=='M' or size=='m':
        bill+=20
       
      else:
       bill +=30
        
else:
      bill=bill
extra=input("Do you want extra size:")
if extra=='yes':
   bill+=20
print("Your amount is ",bill)       
                
