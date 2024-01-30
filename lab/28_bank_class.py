class bank_account:
    def __init__(self):
        self.balance=0
        print("welcome to deposit/withdraw machine ")
    def deposit(self):
        amount=int(input("enter the amount to deposit :"))
        self.balance=self.balance + amount

    def withdraw(self):
        amount=int(input("enter the amount to withdraw :"))
        if(amount<=self.balance):
            self.balance=self.balance-amount
            print("withdrawed amount is ",amount)
        else:
            print("insufficinet balance!")
    def display(self):
        print("available balance is :",self.balance)
    
obj=bank_account()
obj.deposit()
obj.withdraw()
obj.display()