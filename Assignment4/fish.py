from animal import Animal

class Fish(Animal):

    def reproduce(self) -> str:
        return super().reproduce() + ' Fish reproduction varies largely, some give birth to live youngs while others lay eggs.'

    def __repr__(self) -> str:
        return super().__repr__() + '\nClass : Fish'
