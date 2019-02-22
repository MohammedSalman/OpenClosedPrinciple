from menu.bank import BankAccount
from menu.menubuilder import MenuBuilder
from menu.menuitem import MenuItem
import menu.actions


class Teller:
    """This class is the interface to a customer's bank account"""

    def __init__(self):
        # Using composition to establish the relationship between the bank
        # and the teller, as well as the teller and the CLI menu that
        # serves as the UI
        self.account = BankAccount()

        # Initialize the menu builder
        self.menu = MenuBuilder()

        # Iterate over all of the classes in menu.actions package
        for action_class in menu.actions.all_actions.values():
            # Initialize each menu action and pass in the bank account
            action = action_class(self.account)

            # Add the menu action to the menu builder
            self.menu.add(MenuItem(action.prompt, action))

        self.menu.add(MenuItem("Quit", exit))
        self.menu.show()
