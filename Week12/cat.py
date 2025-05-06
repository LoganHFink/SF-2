from animal import Animal

class Cat(Animal):
    def __init__(self):
        # super().__init__(4)
        # or (do the sme thing)
        Animal.__init__(self,4)
        self.type = 'cat'

    # cat.sleep will call this chunk below, overwrites the Animal class method.
    # otherwise calling an animal method on cat will do whatever happens in Animal
    def sleep(self, hours = None):
        if hours == None:
            print('Cats sleep in comfortable places')
        else:
            print(f'Cats can sleep for {hours} daily')
        
    def __repr__(self) -> str:
        return f'Animal: {self.type} \nLegs: {self.legs}'
    
cat = Cat()
print(cat)      # Animal: cat \n Legs: 4

print()

cat.walk() # from Animal
cat.sleep() # from cat
cat.sleep(12) # from cat