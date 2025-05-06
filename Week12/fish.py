from __future__ import annotations

from animal import Animal

class Fish(Animal):
    def __init__(self,colour):
        super().__init__(0)
        self.type = 'fish'
        self.colour = colour

    def walk(self):
        print('Fish do not walk, they swim')

    def sleep(self):
        print('Fish rest by reducing their activity and metabolism')

    def __repr__(self) -> str:
        return f'Animal: {self.type} \nColour: {self.colour}'
    
    def changeColour(self,colour:str):
        self.colour = colour

    def same_colour(self,other_fish:Fish):
        return self.colour == other_fish.colour
    
if __name__ == '__main__':
    fish = Fish('blue')
    print(fish)
    
    print()
    
    fish.sleep()
    fish.walk()
    
    print()

    fish.changeColour('Yellow')
    print(fish)

    fish2 = Fish('blue')
    print(fish.same_colour(fish2))