from animal import Animal

class Reptile(Animal):

    def reproduce(self):
        super().reproduce()
        print('\n')
        print('Reptiles lay eggs on land typically instead of water')

    def __repr__(self) -> str:
        return super().__repr__() + '\nClass : Reptile'