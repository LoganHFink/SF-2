from heterotroph import Heterotroph

class Omnivore(Heterotroph):
    def eat(self) -> None:
        super().eat()
        print('I eat plants and meats.')

    def __repr__(self) -> str:
        return super().__repr__() + '\nThis organism is omnivore, it feeds on plant matter, meat matter and it\'s physiology facilitates food search and murder.'