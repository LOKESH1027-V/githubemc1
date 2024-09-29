def add(n,m):
    return n+m
def mul(n,m):
    return n*m
def sub(n,m):
    return n-m
def div(n,m):
    return n/m
def calculator():
 n=int(input("Entert the first number:"))
 state=True

 while state:
  N={"+":add,
   "-":sub,
   "*":mul,
   "/":div
   }
  for i in N:
    print(i)
  pick=input("pick the operntor:")
  m=int(input("Enter the second number:"))
  cal=N[pick]
  output=cal(n,m)
  print(f"{n} {pick} {m} = {output}")
  next=input(f"Do you want to continue with y{output} or do you want to continue with n or do you want to exit:").lower()
  if next=="y":
    n=output
  elif next=="n":
    state=False
    calculator()
  else:
    state=False     
    print("Bye")
calculator()    


   