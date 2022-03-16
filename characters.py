class Character(object):
    def __init__(self, name, fight, attack, defense):
        self.dead = False
        self.name = name
        self.starting_fight = fight
        self.fight = fight
        self.attack = attack
        self.defense = defense
        
    def __str__(self):
        return f'{self.name} is {"dead" if self.dead else "alive"} with {self.fight} fight remaining\nAttack: {self.attack}\nDefense: {self.defense}\nWins: {self.wins}\nLosses: {len(self.losses)}'
    
    def take_damage(self, damage):
        self.fight -= damage
        
        if self.fight < 1:
            self.dead = True
            
    def revive(self):
        self.dead = False
        self.fight = self.starting_fight
        
class Card(object):
    def __init__(self, name, attack, defense, characters = []):
        self.out_of_play = False
        self.name = name
        self.attack = attack
        self.defense = defense
        self.characters = characters
        self.wins = {'total': 0}
        self.losses = {'total': 0}
        
    def __str__(self):
        return str(self.characters)
    
    def win(self, opponent):
        self.wins['total'] += 1
        
        if opponent.name not in self.wins.keys():
            self.wins[opponent.name] = 1
        else:
            self.wins[opponent.name] += 1
    
    def lose(self, opponent):
        self.losses['total'] += 1
        
        if opponent.name not in self.losses.keys():
            self.losses[opponent.name] = 1
        else:
            self.losses[opponent.name] += 1
    
    def take_damage(self, opponent, damage):
        is_damage_dealt = False
        
        for character in self.characters:
            if not character.dead:
                character.take_damage(damage)
                is_damage_dealt = True
                break
                
        # No characters are alive
        if not is_damage_dealt:
            self.out_of_play = True
            self.lose(opponent)
            opponent.win(self)
            
    def revive(self):
        for character in self.characters:
            character.revive()
        
    def reset(self):
        self.wins = {total: 0}
        self.losses = {total: 0}