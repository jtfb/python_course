class Account:

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f'Account Owner: {self.owner}\nAccount Balance: ${self.balance}'

    def deposit(self, deposit):
        self.balance = self.balance + deposit
        print(self.owner)
        print(f'Deposit of {deposit} Accepted at {self.owner} Account')

    def withdraw(self, withdraw):
        if self.balance >= withdraw:
            self.balance = self.balance - withdraw
            print(f'Withdraw of {withdraw} Accepted at {self.owner} Account')
        else:
            print("Funds Unavailable")

# 1. Instantiate the class
acct1 = Account('Jose',100)

# # 2. Print the object
print(acct1)

# 3. Show the account owner attribute
acct1.owner

# 4. Show the account balance attribute
acct1.balance

# 5. Make a series of deposits and withdrawals
acct1.deposit(50)

acct1.withdraw(75)

# 6. Make a withdrawal that exceeds the available balance
acct1.withdraw(500)