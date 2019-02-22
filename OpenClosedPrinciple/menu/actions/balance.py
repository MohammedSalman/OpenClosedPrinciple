from .action import BaseAction
import os


class ShowBalance(BaseAction):
    def __init__(self, account):
        self.account = account

    @property
    def prompt(self):
        return "Show balance"

    def __call__(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n   Your balance is: {}".format(self.account.show_balance()))
        input(">> Press enter to continue <<")
