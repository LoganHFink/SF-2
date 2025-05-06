from abc import ABCMeta

class Heterotroph(object,metaclass = ABCMeta):
    
    def __init__(self,legs:int=0,fins:int=0,wings:int=0):
        self.legs = legs
        self.fins = fins
        self.wings = wings

    def eat(self) -> None:
        print('I eat other organisms instead of generating my own food')

    def __repr__(self) -> str:
        return 'This organism is a heterotroph, it is unable to make it\'s own food, so it eats people.'