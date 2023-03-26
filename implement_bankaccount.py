class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance

class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate

account1 = Account("Ashish", 5000)


print(account1.title) 
print(account1.balance) 

savingsAccount1 = SavingsAccount("Ashish", 5000, 5)


print(savingsAccount1.title) 
print(savingsAccount1.balance) 
print(savingsAccount1.interestRate) 