class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def get_balance(self):
        """Returns the current balance."""
        return self.balance

    def deposit(self, amount):
        """Deposits money into the account."""
        self.balance += amount

    def withdraw(self, amount):
        """Withdraws money if sufficient balance exists."""
        if self.balance >= amount:
            self.balance -= amount
            return True
        return False
