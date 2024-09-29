a=float(input("Enetr your weight in kg :"))
b=float(input("Enter your height in m :"))
bmi=round(a/b**2)
if bmi<18.5:
    print(f"Your bmi is {bmi} and your are underweight")
elif 18.5<bmi>25.0:
    print(f"Your bmi is {bmi} and your are healthy")     
else:
    print(f"Your bmi is {bmi} and your are obbese")    