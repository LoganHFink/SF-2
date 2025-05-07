from bird import Bird
from pet import Pet
from omnivore import Omnivore

class Parrot(Bird,Omnivore,Pet):
    def __init__(self,legs:int=2,wings:int=2,colour:str='Yellow'):
        Bird.__init__(self,wings,legs)
        self.colour = colour   

    def __repr__(self) -> str:
        # kindom/class, species, 'this animal is a pet', 'this is a heter/this is a carnivore'
        return Bird.__repr__(self) + '\nSpecies : Parrot\n' + Pet.__repr__(self) + '\n\n' + Omnivore.__repr__(self)
    
    def reproduce(self) -> str:
        return Bird.reproduce(self) + ' Parrot take a few to lay a full clutch of eggs. This can be as many three to four eggs.'
    
    def move(self) -> None:
        print('I can move in various ways. I can fly, walk, climb and even use a unique \"beakiation\" to traverse narrow branches.')

    def eat(self) -> None:
        Omnivore.eat(self)
        print('I eat both plant and animal matter. My natural diet includes a variety of foods like seeds, nuts, fruits, vegetables, flowers, buds, and insects.')

    def sleep(self) -> None:
        print('Parrots sleep around 10 to 12 hours each night, often tucked under their wings. Thye may also take naps during the day.')

if __name__ == '__main__':
    p = Parrot(1,2,'red')
    print(p.wings)
    print(p.colour)
    print(p.legs)
    print(p)
    print('------------------------------------------------------------------------------------------------')
    print(p.reproduce())
    print('------------------------------------------------------------------------------------------------')
    p.eat()
    print('------------------------------------------------------------------------------------------------')
    p.move()
    print('------------------------------------------------------------------------------------------------')
    p.sleep()
    print('------------------------------------------------------------------------------------------------')
    print(p.pet())