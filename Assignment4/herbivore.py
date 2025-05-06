from heterotroph import Heterotroph

class Herbivore(Heterotroph):
    def eat(self) -> None:
        super().eat()
        print('I eat plants.')

    def __repr__(self) -> str:
        return super().__repr__() + ' This organism is a herbivore. It feeds on plant matter and its physiology facilitates food search.'