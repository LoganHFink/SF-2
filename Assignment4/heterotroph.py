from abc import ABCMeta,abstractmethod

class Heterotroph(object,metaclass = ABCMeta):
    
    def __init__(self,legs:int=0,fins:int=0):
        self.legs = legs
        self.fins = fins

    def eat(self) -> None:
        print('I eat other organisms instead of generating my own food.')

    def __repr__(self) -> str:
        return 'This organism is a heterotroph, it is unable to produce it\'s own food, so it eats other organisms.'
    
    @abstractmethod
    def move(self) -> None:
        pass
    
    @abstractmethod
    def sleep(self) -> None:
        pass