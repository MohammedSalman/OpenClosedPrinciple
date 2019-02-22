from .action import BaseAction


class Withdraw(BaseAction):
    def __init__(self, account):
        self.account = account

    @property
    def prompt(self):
        return "Withdraw Money"

    def __call__(self):
        amount = input("How much? ")
        # self.account.add_money(amount)
        self.account.withdraw_money(amount)
