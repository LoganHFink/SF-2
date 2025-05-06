from abc import ABCMeta, abstractmethod

class Animal(object,metaclass = ABCMeta):

    def __init__(self,legs:int = 0, fins:int = 0):
        self.legs = legs
        self.fins = fins

    @abstractmethod
    def move(self) -> None:
        pass
    
    @abstractmethod
    def sleep(self) -> None:
        pass

    @abstractmethod
    def eat(self) -> None:
        pass

    def reproduce(self) -> str:
        return 'Members of this kingdom reproduce by finding a mate of the same species.'
    
    def __repr__(self) -> str:
        return 'Kindom : Animalia'
    
