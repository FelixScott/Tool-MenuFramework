# This is a framework for a basic console line menu system to navigate functions
# Each menu screen is stored as its own class object with options passed via the InsertMenuOption
# Each menu can be displayed by calling its Display function
# Each menu should be declared in two 3 steps:
#   1) Create a new class object with the menu name
#       ExampleMenu2 = Menu("ExampleMenu2")
#   2) Define the menus return menu, this allows reverse navigation through the menu system
#       ExampleMenu2.ReturnMenu = ExampleMenu1
#   3) Define each option in the menu and which functions it calls
#       ExampleMenu2.InsertMenuOption("ExampleMenuFunction3", True, ExampleMenuFunction3)
#       ExampleMenu2.InsertMenuOption("ExampleMenuFunction4", True, ExampleMenuFunction4)
#   REMEMBER the previous menu option will be created for you there is no need to do it yourself
# When creating a menu option the second argument passed determines (if true) whether the menu will be displayed again
# once the function is run, make this false when navigating to a new menu screen true when executing a function

class Menu:
    def __init__(self, PassedMenuName):
        self.ReturnMenu = None
        self.MenuOptions = []
        self.MenuName = str(PassedMenuName)

    def InsertMenuOption(self, PassedName, PassedMenuReturn,  PassedFunction):
        TempName = str(PassedName)
        MenuReturn = PassedMenuReturn
        TempFunction = PassedFunction
        self.MenuOptions.append(TempName)
        self.MenuOptions.append(MenuReturn)
        self.MenuOptions.append(TempFunction)

    def Display(self):
        print("\n----------{}----------".format(self.MenuName))
        i = 0
        j = 1
        while i < len(self.MenuOptions):
            print("{}: {}".format(j, self.MenuOptions[i]))
            i += 3
            j += 1
        if self.ReturnMenu is None:
            print("{}: Exit Program".format(j))
        else:
            print("{}: Back".format(j))
        print("----------{}----------".format("-"*len(self.MenuName)))
        print()
        Selection = input("Please Choose from above options: ")
        Selection = int(Selection)
        if Selection == j:
            if self.ReturnMenu is None:
                print("Exiting Program...")
                quit()
            else:
                self.ReturnMenu.Display()
        else:
            Selection = (Selection * 3 - 1)
            print()
            if (self.MenuOptions[Selection-1]) is True:
                self.MenuOptions[Selection]()
                self.Display()
            else:
                self.MenuOptions[Selection]()


# Menu function declarations
def ExampleMenuFunction1():
    print("ExampleMenuFunction1 is executed")


def ExampleMenuFunction2():
    print("ExampleMenuFunction2 is executed")


def ExampleMenuFunction3():
    print("ExampleMenuFunction3 is executed")


def ExampleMenuFunction4():
    print("ExampleMenuFunction4 is executed")


def ExampleMenuFunction5():
    print("ExampleMenuFunction5 is executed")


def ExampleMenuFunction6():
    print("ExampleMenuFunction6 is executed")


# Menu declarations
ExampleMenu1 = Menu("ExampleMenu1")
ExampleMenu2 = Menu("ExampleMenu2")
ExampleMenu2.ReturnMenu = ExampleMenu1
ExampleMenu3 = Menu("ExampleMenu3")
ExampleMenu3.ReturnMenu = ExampleMenu1

# Menu option declarations
ExampleMenu1.InsertMenuOption("ExampleMenuFunction1", True, ExampleMenuFunction1)
ExampleMenu1.InsertMenuOption("ExampleMenuFunction2", True, ExampleMenuFunction2)
ExampleMenu1.InsertMenuOption("DisplayExampleMenu2", False, ExampleMenu2.Display)
ExampleMenu1.InsertMenuOption("DisplayExampleMenu3", False, ExampleMenu3.Display)
ExampleMenu2.InsertMenuOption("ExampleMenuFunction3", True, ExampleMenuFunction3)
ExampleMenu2.InsertMenuOption("ExampleMenuFunction4", True, ExampleMenuFunction4)
ExampleMenu3.InsertMenuOption("ExampleMenuFunction5", True, ExampleMenuFunction5)
ExampleMenu3.InsertMenuOption("ExampleMenuFunction6", True, ExampleMenuFunction6)
ExampleMenu1.Display()
