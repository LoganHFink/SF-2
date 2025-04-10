from __future__ import annotations
from functools import total_ordering

@total_ordering
class Account:
    def __init__(self,gold):
        '''
        Create account with gold
        '''
        self.gold = gold
    
    def addGold(self,amount:int) -> None:
        self.gold += amount
    
    def zeroGold(self) -> None:
        self.gold = 0

    def doubleGold(self) -> None:
        self.gold *= 2

    def __lt__(self, other: Account) -> bool:
        '''
        retrun true if account and other are of same type and self < other
        '''
        return isinstance(other,Account) and self.gold < other.gold
    
    def __eq__(self,other: Account) -> bool:
        return isinstance(other,Account) and self.gold == other.gold

    def __repr__(self) -> str:
        return f'Gold: {self.gold}'
      

################
# Main Program #

a1 = Account(500)
a2 = Account(500)
a3 = Account(56)
a4 = Account(34)
value = 500

print('a4 <? a3: ', a4 < a3)
print('a1 <? a4: ', a1 < a4)
print('a1 ==? a2: ', a1 == a2)
print('a1 ==? a3: ', a1 == a3)
print('a1 ==? value: ', a1 == value)
print()
print('a1 >? a3: ', a1 > a3)
print('a1 >? a2: ', a1 > a2)
print('a1 >=? a2: ', a1 >= a2)

print(a1)