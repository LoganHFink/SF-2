from heterotroph import Heterotroph

class Carnivore(Heterotroph):
    def eat(self) -> None:
        super().eat()
        print('I eat meats.')

    def __repr__(self) -> str:
        return super().__repr__() + '\nThis organism is Carnivore, it feeds on meat matter and it\'s physiology facilitates murder.'