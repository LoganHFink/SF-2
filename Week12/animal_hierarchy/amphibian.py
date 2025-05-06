from animal import Animal

class Amphibian(Animal):

    def reproduce(self):
        super().reproduce()
        print('\n')
        print('Amphibians makes eggs in soft water')

    def __repr__(self) -> str:
        return super().__repr__() + '\nClass : amphibian'
