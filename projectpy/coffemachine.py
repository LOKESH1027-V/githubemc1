
menu={
  "latte":{
    "ingrediant":{
      "water":200,
      "milk":150,
      "coffee":24,
    },
    "cost":150
  },
    "expresso":{
    "ingrediant":{
      "water":50,
      "coffee":18,
    },
    "cost":100
  },
    "cappaccino":{
    "ingrediant":{
      "water":250,
      "milk":100,
      "coffee":24,
    },
    "cost":200
  }
}
profit=0
resourece={
  "water":500,
  "coffee":75,
  "milk":5000,
  "Money":0
}
def check(order,resource):
   for i in order:
      if order[i]>resource[i]:
         print(f"Sorry we don't have enought {order[i]}")
         return False
      return True
def process_coin():
   print("Please insert coin:")
   total=0
   five=int(input("How many five rupee coin:"))
   ten=int(input("How many ten rupee coin:"))  
   twenty=int(input("How many twenty rupee coin:"))
   total=((five*5)+(ten*10)+(twenty*20))
   return total
def check_payment(order,payment):
   if order>=payment:
      global profit
      profit+=order
      changr=payment
      print(f"Here is your change {changr}")
      return True
   else:
      print("The money is not enought")
      return False
def make_coffee(choice,tpye):
   for i in tpye:
      tpye[i]-=choice[i]
   print(f"Here is your coffee {choice}")   
is_on=True
while is_on:
 choice=input("What would you like to have?(latte,expresso,cappaccino)").lower()
 if choice=="off":
    is_on=False
 elif choice=="report":
   print(f" Water={resourece['water']}ml \n Coffee={resourece['coffee']}g \n Milk={resourece['milk']}ml \n Money=Rs{resourece['Money']}")
 else:
     coffee_type=menu[choice]
     print(coffee_type)
     if check(coffee_type["ingrediant"],resourece):
        payment=process_coin()
        if check_payment(coffee_type['cost'],payment):
           make_coffee(choice,coffee_type['ingrediant'])
           
           
