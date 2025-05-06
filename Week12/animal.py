class Animal:
    def __init__(self,legs=0):
        self.legs = legs

    def walk(self):
        print(f'This animal walks with their {self.legs} legs')

    def sleep(self):
        print(f'Different animals have different sleeping habits')

    def __repr__(self) -> str:
        return f'no idea \nlegs: {self.legs}'
    

# this if statement checks if the script being run is this program or just the file being called somewhere else
# without this, in cat.py, when calling Animal all this will print also
   
if __name__ == '__main__':
    anim = Animal(6)
    print(anim)

    print()
    anim.walk()
    anim.sleep()