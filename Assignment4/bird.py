from animal import Animal

class Bird(Animal):
    def __init__(self,wings,legs):
        self.wings = wings
        super().__init__(legs)
    
    def reproduce(self) -> str:
        return super().reproduce() + ' Members of this kingdom reproduce by finding a mate of the same species. Birds typically reproduce by hatching and incubating their eggs.'

    def __repr__(self) -> str:
        return super().__repr__() + '\nClass : Bird'
