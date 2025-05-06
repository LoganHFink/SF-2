from animal import Animal

class Fish(Animal):

    def reproduce(self):
        super().reproduce()
        print('\n')
        print('Fish reproduce with eggs or birth youngins')

    def __repr__(self) -> str:
        return super().__repr__() + '\nClass : Fish'
