from animal import Animal

class Mammal(Animal):

    def reproduce(self) -> str:
        return super().reproduce() + ' Mammals give birth to live young, and raise them until they can be independent.'

    def __repr__(self) -> str:
        return super().__repr__() + '\nClass : Mammal'
    