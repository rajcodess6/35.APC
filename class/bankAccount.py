class BankAccount:
    counter = 1000

    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0
        BankAccount.counter += 1
        self.account_number = BankAccount.counter

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Amount deposited:", amount)

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn:", amount)
        else:
            print("Insufficient balance!")

    def display_balance(self):
        print(self.account_holder, "Balance:", self.balance)

    def transfer(self, amount, other_account):
        if 0 < amount <= self.balance:
            self.balance -= amount
            other_account.balance += amount
            print("Transfer successful:", amount)
        else:
            print("Insufficient balance for transfer!")


a1 = BankAccount("Rahul")
a2 = BankAccount("Priya")

print("Account Number:", a1.account_number)
print("Account Number:", a2.account_number)

a1.deposit(5000)
a1.withdraw(1000)
a1.transfer(2000, a2)

a1.display_balance()
a2.display_balance()