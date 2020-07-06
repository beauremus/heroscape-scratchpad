import random

class Die:
    'a class representing a Die'
    def __init__(self, sides=6, threshold=1):
        'initialize a die, default 6 sides'
        self.sides = sides
        self.threshold = threshold
        self.roll()
        
    def __mul__(self, n):
        return [self.__class__(self.sides, self.threshold) for x in range(n)]

    def roll(self):
        'roll the dice'
        self.dieRoll = random.randint(1, self.sides)
        
class DiceShaker(object):
    def __init__(self, dice=()): # Note we avoid mutable default arguments
        self.dice = list(dice)   # Presumably it would be nice to add/remove dice

    def shake(self):
        for die in self.dice:
            die.roll()

    def get_dice(self):
        return [die.dieRoll for die in self.dice]
    
    def get_successes(self):
        return [die.dieRoll >= die.threshold for die in self.dice].count(True)