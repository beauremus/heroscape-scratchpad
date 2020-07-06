from dice import Die
from dice import DiceShaker

class HeadToHead(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
        self.first_damage_done = 0
        self.second_damage_done = 0
        self.rounds = 0
        self.winner = 'No battle yet'
        
    def __str__(self):
        return f'Head to head rounds: {self.rounds}\n{self.first.name}:\n\tDamage done: {self.first_damage_done}\n{self.second.name}:\n\tDamage done: {self.second_damage_done}\nThe winner is: {self.winner}'
    
    def resolve(self):
        first_attack_dice=DiceShaker(Die(6, 4) * self.first.attack)
        first_defense_dice=DiceShaker(Die(6, 5) * self.first.defense)
        second_attack_dice=DiceShaker(Die(6, 4) * self.second.attack)
        second_defense_dice=DiceShaker(Die(6, 5) * self.second.defense)
        
        while not self.first.out_of_play and not self.second.out_of_play:
            first_attack_dice.shake()
            second_defense_dice.shake()
            second_attack_dice.shake()
            first_defense_dice.shake()
            
            if first_attack_dice.get_successes() > second_defense_dice.get_successes():
                damage = first_attack_dice.get_successes() - second_defense_dice.get_successes()
                self.first_damage_done += damage
                self.second.take_damage(self.first, damage)
                
            if not self.second.out_of_play and second_attack_dice.get_successes() > first_defense_dice.get_successes():
                damage = second_attack_dice.get_successes() - first_defense_dice.get_successes()
                self.second_damage_done += damage
                self.first.take_damage(self.second, damage)
                
            self.rounds += 1
            
        if self.first.out_of_play:
            self.winner = self.second.name
        else:
            self.winner = self.first.name