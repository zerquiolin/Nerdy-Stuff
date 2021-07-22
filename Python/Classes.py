class Account:
    
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def __str__(self):
        return f"Account owner:   {self.owner}\nAccount balance: ${self.balance}"

    def deposit(self, ammount):
        self.balance += ammount
    
    def withdraw(self, ammount):
        if ammount > self.balance:
            print('Funds Unavailable!')
        else:
            self.balance -= ammount
            print('Withdrawal Accepted')



acct1 = Account('Jose',100)
print(acct1)
acct1.deposit(50)
acct1.withdraw(75)
acct1.withdraw(500)