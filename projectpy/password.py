import random
letter1=('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
numbers=('1','2','3','4','5','6','7','8','9','0')

special=('!','@','#','$','%','^','&','*','+',',','.')
print("Welcome to password generator")
a=int(input("How many letters do you want:"))
b=int(input("how many numbers do you want:"))
c=int(input("How many specialcharacter do you want:"))
letter=""
p=[]
for i in range(0,a):
    char=random.choice(letter1)
    p.append(char)
for i in range(0,b):
    n=random.choice(numbers)
    p.append(n)
for i in range(0,c):
    c=random.choice(special)
    p.append(c)
print(f"Without shuffle passcharacter in list{p}")    
random.shuffle(p)
print(f"With shuffle password character in list{p}")
d=""
for i in p:
    d=d+i   
print(f"Your final password is {d}")       

