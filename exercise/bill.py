import random
Names=input("Enter names that are separated by cama:")
bill=Names.split(",")
random.shuffle(bill)
a=bill[0]
print(f"{a} is going to pay the bill")