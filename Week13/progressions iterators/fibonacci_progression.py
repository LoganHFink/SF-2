from progression import Progression

class FibonacciProgression(Progression):

    def __init__(self,first = 0, second = 1):
        super().__init__(first) # start progression at first
        self._prev = second - first # value preceding first

    def _advance(self):
        self._current, self._prev = self._prev + self._current, self._current # turn current into previous, make new value for current from sum

if __name__ == '__main__':
    FibonacciProgression().printProgression(10)
    FibonacciProgression(11,22).printProgression(10)