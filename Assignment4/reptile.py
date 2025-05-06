from animal import Animal

class Reptile(Animal):

    def reproduce(self) -> str:
        return super().reproduce() +  ' Reptiles reproduce by laying eggs typically on land rather than in water.'

    def __repr__(self) -> str:
        return super().__repr__() + '\nClass : Reptile'