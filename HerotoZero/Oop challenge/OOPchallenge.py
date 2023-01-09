class Account:

    def __init__(self,owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self,deposit):
        self.balance = self.balance + deposit
        print("Deposit accepted")

    def withdraw(self,withdraw):
        if self.balance >= withdraw :
            self.balance = self.balance - withdraw
            print("Withdrawl accepted ")
        else:
            print("Funds unavailable")

    def __str__(self):
        return "Account owner: %s \nAccount balance: %s" %(self.owner,self.balance)


# Instantiate the class
acct1 = Account('Jose',100)
print(acct1)
print(acct1.owner)
print(acct1.balance)
acct1.deposit(50)
acct1.withdraw(75)
acct1.withdraw(500)