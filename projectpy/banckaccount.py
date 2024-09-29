class banckaccount():
    def __init__(self,name,ammount=0):
        self.name=name
        self.balance=ammount
    def deposite(self,deposite):
        self.balance=deposite+self.balance
        print(f"{self.balance} to your account")
    def withdraw(self,withdraw):
        if withdraw<self.balance:
            self.balance=self.balance-withdraw
            print(f"Sucessfully withdraw")
            print(f"Balance :{self.balance}")
        else:
            print(f"You don't have enought money")
    def __str__(self):
        return f"Account Holder name :{self.name} \nAmmount : {self.balance}"
obj=banckaccount("Lokesh",2000)
print(obj)
obj.deposite(200)
obj.withdraw(2000)