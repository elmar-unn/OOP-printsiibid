from abc import ABC

class Creature:
    def __init__(self, attack, health):
        self.attack = attack
        self.health = health


class CardGame(ABC):
    def __init__(self, creatures):
        self.creatures = creatures
        
    def combat(self, c1_index, c2_index):
        c1 = self.creatures[c1_index]
        c2 = self.creatures[c2_index]

        c1_alive = self.hit(c1, c2)
        c2_alive = self.hit(c2, c1)

        if c1_alive and c2_alive:
            return -1
        if not c1_alive and not c2_alive:
            return -1
        if c1_alive:
            return c1_index
        return c2_index

    def hit(self, attacker, defender):
        pass


class TemporaryDamageCardGame(CardGame):
    def hit(self, attacker, defender):
        original_health = defender.health

        defender.health -= attacker.attack

        if defender.health > 0:
            defender.health = original_health  # taastub
            return True
        return False


class PermanentDamageCardGame(CardGame):
    def hit(self, attacker, defender):
        defender.health -= attacker.attack
        return defender.health > 0