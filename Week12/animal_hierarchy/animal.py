from abc import ABCMeta, abstractmethod

class Animal(object,metaclass = ABCMeta):

    def __init__(self,legs:int = 0, fins:int = 0, wings:int = 0):
        self.legs = legs
        self.fins = fins
        self.wings = wings

    @abstractmethod
    def move(self) -> None:
        pass
    
    @abstractmethod
    def sleep(self) -> None:
        pass

    @abstractmethod
    def eat(self) -> None:
        pass

    def reproduce(self) -> None:
        print('Members of this kingdom reproduce by finding a mate of the same species')
    
    def __repr__(self) -> str:
        return 'Kindom : Animalia'
    
# if __name__ == '__main__':
#     anim = Animal(1,2,3)
#     #this wont run, CANT INITIATE ABSTRACT CLASS