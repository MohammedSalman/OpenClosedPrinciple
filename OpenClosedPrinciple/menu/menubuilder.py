import os


class MenuBuilder:
    """Responsible for building a command line menu system from MenuItems"""

    def __init__(self, *args):
        self.__menu = list()

        for item in args:
            self.__menu.append(item)

    def add(self, menu_item=None, menu_items=None):
        if menu_items is not None:
            self.__menu.extend(menu_items)

        if menu_item is not None:
            self.__menu.append(menu_item)

    def show(self):
        # Clear the console
        os.system('cls' if os.name == 'nt' else 'clear')

        # Display each menu item
        for index, menu_item in enumerate(self.__menu):
            try:
                print("{}. {}".format(index + 1, menu_item.prompt))
            except AttributeError:
                raise AttributeError('Could not display the prompt for the current menu item {}'.format(str(menu_item)))

        try:
            choice = int(input(">> "))

            # Invoke the class corresponding to the choice
            for menu_item in self.__menu:
                if choice == self.__menu.index(menu_item) + 1:
                    menu_item.action()

        except KeyboardInterrupt:  # Handle ctrl+c
            exit()

        except ValueError:  # Handle any invalid choice
            pass

        self.show()  # Display the MenuItems
