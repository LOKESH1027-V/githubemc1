def prime(number):
  is_prime=True
  for i in range(2,number): 
    if number%i==0:
       is_prime=False
  if is_prime:
      print(f"The number {number} is prime")
  else:
      print(f"The number {number} is not prime")  
n=[]     
m=int(input('Enter:'))
for i in range(1,m,+1):
   n.append(i)
print(n)   