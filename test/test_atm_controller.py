from contextlib import AbstractContextManager
from typing import Any
from atm import ATMController, BankAPI, Account, Card
from atm import CardNotRegisteredError, AccountNotExistError
import unittest

class TestATMController(unittest.TestCase):
    def setUp(self):
        self.bank_api = BankAPI()
        cards_data = {
            '1111-1111-1111-1111': [('10000001', 1000)],
            '1111-1111-1111-2222': [('20000001', 2000), ('20000002', 5000)],
            '1111-1111-1111-3333': [('30000001', 1500), ('30000002', 45000), ('30000003', 25000)],
            '1111-1111-1111-4444': [('40000001', 100), ('40000002', 15000)],
            '1111-1111-1111-5555': [('50000001', 10), ('50000002', 800)],
            '1111-1111-1111-6666': [('60000001', 100000), ('60000002', 500000)],
            '1111-1111-1111-7777': [('70000001', 40000), ('70000002', 50)],
            '1111-1111-1111-8888': [('80000001', 2020200), ('80000002', 5030)],
            '1111-1111-1111-9999': [('90000001', 100)]
        }
        for i, (card_number, accounts_data) in enumerate(cards_data.items(), start=1):
            accounts = [Account(account_number, balance) for account_number, balance in accounts_data]
            card = Card(card_number, accounts)
            pin = f'123{i}'  # Generate a simple PIN like '1231', '1232', etc.
            self.bank_api.register_card(card, pin)

        self.atm = ATMController(self.bank_api)


    def test_insert_card_1(self):
        self.atm.insert_card('1111-1111-1111-1111')
        self.assertEqual(self.atm.current_card.card_number, '1111-1111-1111-1111')

    def test_insert_card_2(self):
        self.atm.insert_card('1111-1111-1111-2222')
        self.assertEqual(self.atm.current_card.card_number, '1111-1111-1111-2222')

    def test_insert_unregistered_card(self):
        with self.assertRaises(CardNotRegisteredError):
            self.atm.insert_card('9999-9999-9999-9999')
        
    def test_enter_pin_correct(self):
        self.atm.insert_card('1111-1111-1111-1111')
        self.assertTrue(self.atm.enter_pin('1231'))

    def test_enter_pin_incorrect(self):
        self.atm.insert_card('1111-1111-1111-1111')
        self.assertFalse(self.atm.enter_pin('4321'))

    def test_select_account(self):
        self.atm.insert_card('1111-1111-1111-1111')
        self.atm.enter_pin('1231')
        self.atm.select_account('10000001')
        self.assertEqual(self.atm.current_account.account_number, '10000001')

    def test_select_unassociated_account(self):
        self.atm.insert_card('1111-1111-1111-1111')
        self.atm.enter_pin('1231')
        with self.assertRaises(AccountNotExistError):
            self.atm.select_account('87654321')

    def test_balance_check(self):
        self.atm.insert_card('1111-1111-1111-1111')
        self.atm.enter_pin('1231')
        self.atm.select_account('10000001')
        self.assertEqual(self.atm.check_balance(), 1000)

    def test_deposit(self):
        self.atm.insert_card('1111-1111-1111-1111')
        self.atm.enter_pin('1231')
        self.atm.select_account('10000001')
        self.atm.deposit(500)
        self.assertEqual(self.atm.check_balance(), 1500)

    def test_withdraw(self):
        self.atm.insert_card('1111-1111-1111-1111')
        self.atm.enter_pin('1231')
        self.atm.select_account('10000001')
        self.atm.withdraw(200)
        self.assertEqual(self.atm.check_balance(), 800)

    def test_withdraw_insufficient_funds(self):
        self.atm.insert_card('1111-1111-1111-1111')
        self.atm.enter_pin('1231')
        self.atm.select_account('10000001')
        self.assertFalse(self.atm.withdraw(2000))

if __name__ == '__main__':
    unittest.main()
