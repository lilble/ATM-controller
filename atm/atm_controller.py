class CardNotRegisteredError(Exception):
    """Raised when a card is not registered in the system."""
    pass

class AccountNotExistError(Exception):
    """Raised when an account does not exist for the card."""
    pass

class UnexpectedError(Exception):
    """Raised when an unexpected error occurs."""
    pass

class ATMController:
    def __init__(self, bank_api):
        self.bank_api = bank_api
        self.current_card = None
        self.current_account = None

    def insert_card(self, card_number):
        """Inserts a card into the ATM."""
        if not self.bank_api.card_registered(card_number):
            raise CardNotRegisteredError(f"Card {card_number} is not registered.")
        self.current_card = self.bank_api.get_card(card_number)
        print(f"Card {card_number} inserted.")

    def enter_pin(self, pin):
        """Verifies PIN for the current card."""
        if not self.current_card:
            raise UnexpectedError("Card not inserted.")
        if self.bank_api.verify_pin(self.current_card, pin):
            print("PIN is correct.")
            return True
        else:
            print("PIN is incorrect.")
            return False

    def select_account(self, account_number):
        """Selects the current account."""
        if not self.current_card:
            raise UnexpectedError("Card not inserted.")
        if not self.current_card.has_account(account_number):
            raise AccountNotExistError("Account not associated with the card.")
        self.current_account = self.current_card.get_account(account_number)
        print(f"Account {account_number} selected.")

    def check_balance(self):
        """Returns the balance of the current account."""
        if not self.current_account:
            raise UnexpectedError("Account not selected.")
        return self.current_account.get_balance()

    def deposit(self, amount):
        """Deposits money into the current account."""
        if not self.current_account:
            raise UnexpectedError("Account not selected.")
        if amount <= 0:
            print("Deposit amount must be greater than 0.")
            return False    
        self.current_account.deposit(amount)
        print(f"${amount} deposited. New balance: {self.check_balance()}")
        return True

    def withdraw(self, amount):
        """Withdraws money from the current account."""
        if not self.current_account:
            raise UnexpectedError("Account not selected.")
        if self.current_account.withdraw(amount):
            print(f"${amount} withdrawn. New balance: {self.check_balance()}")
            return True
        else:
            print(f"Insufficient funds. Current balance: {self.check_balance()}")
            return False