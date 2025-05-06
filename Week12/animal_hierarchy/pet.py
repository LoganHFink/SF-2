from abc import ABCMeta

class Pet(object,metaclass = ABCMeta):
    def __init__(self,legs:int=0,fins:int=0,wings:int=0):
        self.legs = legs
        self.fins = fins
        self.wings = wings

    def pet(self) -> str:
        return 'You can pet this animal!!!'
    
    def __repr__(self) -> str:
        return 'This animal is a pet.'