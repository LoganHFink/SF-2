from mammal import Mammal
from pet import Pet
from omnivore import Omnivore

class Dog(Mammal,Omnivore,Pet):
    def __init__(self,legs:int=4,ears:int =2):
        # super().__init__(legs)
        # OR DO THIS:
        Mammal.__init__(self,legs=legs)
        self.ears = ears

    def __repr__(self) -> str:
        # kindom, class, species, 'this animal is a pet', 'this is a carnivore'
        return Mammal.__repr__(self) + '\nSpecies : Dog\n' + Pet.__repr__(self) + '\n' + Omnivore.__repr__(self)
    
    def reproduce(self) -> None:
        Mammal.reproduce(self)
        print('Dogs make cute little puppies.')
    
    def move(self) -> None:
        print('Dogs move with they legs.')

    def eat(self) -> None:
        Omnivore.eat(self)
        print('Dogs eat all sorts of things with their mouths!')

    def sleep(self) -> None:
        print('Dogs take lots of naps.')

if __name__ == '__main__':
    b1 = Dog()
    print(b1)
    print()
    b1.eat()
    print()
    b1.reproduce()
    print()
    b1.sleep()
    print()
    b1.move()
    print()
    print(b1.pet())