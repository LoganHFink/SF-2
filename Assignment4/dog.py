from mammal import Mammal
from pet import Pet
from omnivore import Omnivore

class Dog(Mammal,Omnivore,Pet):
    def __init__(self,legs:int=4,ears:int =2):
        Mammal.__init__(self,legs=legs)
        self.ears = ears

    def __repr__(self) -> str:
        # kindom/class, species, 'this animal is a pet', 'this is a heter/this is a carnivore'
        return Mammal.__repr__(self) + '\nSpecies : Dog\n' + Pet.__repr__(self) + '\n\n' + Omnivore.__repr__(self)
    
    def reproduce(self) -> str:
        return Mammal.reproduce(self) + ' Dogs give birth to litters of cute little puppies.'
    
    def move(self) -> None:
        print('Dogs get the zoomies and run around with their legs.')

    def eat(self) -> None:
        Omnivore.eat(self)

    def sleep(self) -> None:
        print('Dogs take lots of naps to regain their energy.')

if __name__ == '__main__':
    d = Dog()
    print(d)
    print('------------------------------------------------------------------------------------------------')
    print(d.reproduce())
    print('------------------------------------------------------------------------------------------------')
    d.eat()
    print('------------------------------------------------------------------------------------------------')
    d.move()
    print('------------------------------------------------------------------------------------------------')
    d.sleep()
    print('------------------------------------------------------------------------------------------------')
    print(d.pet())