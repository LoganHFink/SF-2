from progression import Progression

class GeometricProgression(Progression):

    def __init__(self,base=2,start=1):
        super().__init__(start)
        self._base = base

    def _advance(self):
        self._current *= self._base

if __name__ == '__main__':
    GeometricProgression(base = 3,start = 4).printProgression(7)