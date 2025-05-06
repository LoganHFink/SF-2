from heterotroph import Heterotroph

class Carnivore(Heterotroph):
    def eat(self) -> None:
        super().eat()
        print('I eat meats.')

    def __repr__(self) -> str:
        return super().__repr__() + ' This organism is a carnivore. It feeds on other animals, and its physical features facilitate hunting.'