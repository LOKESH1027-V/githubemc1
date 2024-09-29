alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def encript(text,shift_number):
    chiper=""
    for char in text:
        if char in alphabet:
         position=alphabet.index(char)
         new=(position+shift_number)%25
         chiper+=alphabet[new]
        else:
           chiper+=char 
    print(f"Here is the twxt after encription:{chiper}")
def decript(text,shift_number):
    chiper=""
    for char in text:
        if char in alphabet:
         position=alphabet.index(char)
         new=(position-shift_number)%25 
         chiper+=alphabet[new]
        else:
           chiper+=char 
    print(f"Here the  text after decription:{chiper}")

wanna_end=False
while not wanna_end:
    What_To_Do=input("type encript for encription,type decript for decription:")
    text=input("Enter your text:").lower()
    shift=int(input("Enter the shift number:"))
    if What_To_Do=="encript":
       encript(text=text,shift_number=shift)
    elif What_To_Do=="decript":
       decript(text=text,shift_number=shift)    
    how=input("type yes to stop, type no to continue:")
    if  how=="yes":
        wanna_end=True 
        print("Enjoy your day with smile.")
  