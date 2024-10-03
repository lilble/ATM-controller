class Card:
    def __init__(self, card_number, accounts):
        self.card_number = card_number
        self.accounts_db = {account.account_number: account for account in accounts}

    def has_account(self, account_number):
        return account_number in self.accounts_db
    
    def get_account(self, account_number):
        return self.accounts_db.get(account_number)