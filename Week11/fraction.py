from __future__ import annotations
from functools import total_ordering
import math
import random
# Create a  fraction class that defines a rational number
# define a constructor with default values (unless the user provides an input) for numerator and denominator 0 and 1
# if numerator is 0, numerator should be 1
# determine the sign of the fraction
# make sure it's in reduced form

@total_ordering
class Fraction:

    def __init__(self, numerator:int = 0, denominator = 1):
        if denominator == 0:
            raise ZeroDivisionError("Don't 0")
        numerator = numerator * (denominator / abs(denominator))
        gcd = math.gcd(int(numerator), denominator) 
        if gcd != 1:
            numerator //= gcd
            denominator //= gcd
        self.numerator = int(numerator)
        self.denominator = abs(denominator)
        
        if numerator == 0:
            self.denominator = 1
        
    def __repr__(self):
        return f"{self.numerator}/{self.denominator}"

    def __add__(self,other_frac) -> Fraction:
        numerator = self.numerator*other_frac.denominator + other_frac.numerator*self.denominator
        denominator = self.denominator*other_frac.denominator
        return Fraction(numerator, denominator)
    
    def __sub__(self,other_frac) -> Fraction:
            numerator = self.numerator*other_frac.denominator - other_frac.numerator*self.denominator
            denominator = self.denominator*other_frac.denominator
            return Fraction(numerator, denominator)
    
    def __eq__(self,other_frac) -> Fraction:
         return self.denominator == other_frac.denominator and self.numerator == other_frac.numerator
    
    def __ge__(self,other_frac) -> Fraction:
         return self.numerator / self.denominator > other_frac.numerator / other_frac.denominator

    def __float__(self) -> float:
         return self.numerator/self.denominator

# Main Program

list = [Fraction(random.randint(-100,100),random.randint(-100,100)) for i in range(10)]
print('unsorted list: ',list)
print('sorted list: ',sorted(list,key=float,reverse=True))