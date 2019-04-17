# kittystuff: what do cats care about

class KittyStuff:
    def __init__(self):
        self.lives = 9
        self.enemies = []
        self.enemies.append('dog')
        self.happiness = 0

    def purr(self,happiness_level=0):
        purring = 'purr'
        for i in range(0, happiness_level):
            purring += '!'
        return purring

    def set_happiness(self, new_happiness):
        self.happiness = new_happiness

    def let_owner_sleep(self):
        return self.happiness < 5
