class Bank:
    def __init__(self,id,name,balance):
        self.id= id
        self.name=name
        self.balance= balance
    
    def cusinfo(self):
        print(f"customer id:{self.id}")
        print(f"customer name:{self.name}")
        print(f"balance amount:{self.balance}")
    
    def deposite(self,amount):
        self.balance+=amount
        print(f"{amount} deposited")
        return self.balance
    
    def withdraw(self,amount):
        if self.balance<amount:
            print(f"your balance is below {amount} , please check once")
        else:
            self.balance-=amount
            print(f"you with draw {amount} sucessfully")
        return self.balance
    
    def checkBalance(self):
        print(f"your balance is:{self.balance}")

id = int(input("enter cus id:"))
name=input("enter cus name:")
balance = int(input("enter intial balance:"))

bank = Bank(id,name,balance)
choice=0
while(choice != 5):
    print("1: cus info | 2: deposite | 3: withdraw | 4: check balance | 5: exit")
    choice =int(input())
    if choice==1:
        bank.cusinfo()
        print("===========================================")
    elif choice==2:
        cash = int(input("enter deposite amount:"))
        bank.deposite(cash) 
        print("===========================================")
    elif choice==3:
        cash = int(input("enter amount:"))
        bank.withdraw(cash)
        print("===========================================")
    elif choice == 4:
        bank.checkBalance()
        print("===========================================")
    elif choice != 5:
        print("invalid input")
        print("===========================================")
        
print("Thank you")
    


