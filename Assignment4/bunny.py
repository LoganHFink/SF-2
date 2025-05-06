from mammal import Mammal
from pet import Pet
from herbivore import Herbivore

class Bunny(Mammal,Herbivore,Pet):
    def __init__(self,legs:int=4,ears:int=2):
        Mammal.__init__(self,legs=legs)
        self.ears = ears

    def __repr__(self) -> str:
        # kindom/class, species, 'this animal is a pet', 'this is a hetero/this is a herbivore'
        return Mammal.__repr__(self) + '\nSpecies : Bunny\n' + Pet.__repr__(self) + '\n\n' + Herbivore.__repr__(self)
    
    def reproduce(self) -> str:
        return Mammal.reproduce(self) + ' Bunnies can produce multiple litters per year, potentially having 3-8 kids per litter.'
    
    def move(self) -> None:
        print('I move by hopping and I can see behind me...')

    def eat(self) -> None:
        Herbivore.eat(self)
        print('I mostly eat fresh hay and grass, with some leafy greens and a few pellets. I should only be given fruit and root vegetables, like carrots, as an occasional treat')

    def sleep(self) -> None:
        print('Bunnies as nocturnal animals typically sleep between 12 to 14 hours a day in short, intermittent periods.')

if __name__ == '__main__':
    b = Bunny()
    print(b)
    print('------------------------------------------------------------------------------------------------')
    print(b.reproduce())
    print('------------------------------------------------------------------------------------------------')
    b.eat()
    print('------------------------------------------------------------------------------------------------')
    b.move()
    print('------------------------------------------------------------------------------------------------')
    b.sleep()
    print('------------------------------------------------------------------------------------------------')
    print(b.pet())