from abc import ABCMeta,abstractmethod

class Pet(object,metaclass = ABCMeta):
    def __init__(self,legs:int=0):
        self.legs = legs

    def pet(self) -> str:
        return 'You can pet this animal!'
    
    def __repr__(self) -> str:
        return 'This animal is a pet!'
    
    @abstractmethod
    def move(self) -> None:
        pass
    
    @abstractmethod
    def sleep(self) -> None:
        pass

    @abstractmethod
    def eat(self) -> None:
        pass
