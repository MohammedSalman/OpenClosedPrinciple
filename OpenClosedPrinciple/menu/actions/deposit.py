from .action import BaseAction


class Deposit(BaseAction):
    def __init__(self, account):
        self.account = account

    @property
    def prompt(self):
        return "Add Money"

    def __call__(self):
        amount = input("How much? ")
        self.account.add_money(amount)
