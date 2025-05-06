from __future__ import annotations
from functools import total_ordering

class Menu:
    def __init__(self):
        self.options = []

    def addOption(self,option:str):
        self.options.append(option)

    def getInput(self)->int:
        for i in range(len(self.options)):
            print(f'{i+1}) {self.options[i]}')
        done = False
        while not done:
            try:
                choice = int(input('choose option '))
                if 0 < choice <= i+1:
                    return choice
            except ValueError:
                print('invalid choice')

# Main

# menu1 = Menu()
# menu1.addOption('Drink')
# menu1.addOption('Side Dish')
# menu1.addOption('Main Dish')
# menu1.addOption('Dessert')
# menu1.addOption('Quit')

# menu1.getInput()
