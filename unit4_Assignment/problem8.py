# 8. What is data hiding in Python? Explain with an example where a class BankAccount hides the balance and provides methods to access or modify it. 

class BankAccount:
    def __init__(self, first_balance):
        self.__balance = first_balance

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("There is not enough balance.")
account = BankAccount(10000)
print("Total balance is:", account.get_balance())

account.deposit(6000)
print("The balance after deposit is:", account.get_balance())

account.withdraw(8000)
print("The balance after withdraw is:", account.get_balance())

