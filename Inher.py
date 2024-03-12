class MagicCard:
    def __init__(self):
        self.dollarCost = 0
        self.colorCombination = ""
        self.name = ""
        self.manaProduced = ""
        
    def __repr__(self):
        return self.name + "costs $" + str(self.dollarCost)

    def __add__(self, other):
        return "It costs $" + str(self.dollarCost + other.dollarCost) + " to buy both " + self.name + " and " + other.name

    def __sub__(self, other):
        if self.dollarCost > other.dollarCost:
            return self.name + " costs $" + str(self.dollarCost - other.dollarCost) + " more than " + other.name
        elif self.dollarCost < other.dollarCost:
            return other.name + " costs $" + str(other.dollarCost - self.dollarCost) + " more than " + self.name
        else:
            return self.name + " and " + other.name + " both cost $" + str(self.dollarCost)

class Land(MagicCard):
    def __init__(self, dc, mp, n):
        MagicCard.__init__(self)
        self.dollarCost = dc
        self.manaProduced = mp
        self.name = n

    def __repr__(self):
        return self.name + " is a land that taps for " + self.manaProduced + " and costs $" + str(self.dollarCost)

class Spell(MagicCard):
    def __init__(self, dc, c, n, mc):
        MagicCard.__init__(self)
        self.dollarCost = dc
        self.colorCombination = c
        self.name = n
        self.manaCost = mc
    
    def __repr__(self):
        return self.name + " is a " + self.colorCombination + " spell with a mana cost of " + self.manaCost + " that costs $" + str(self.dollarCost)

class Permanent(Spell):
    def __init__(self, dc, c, n, mc):
        Spell.__init__(self, dc, c, n, mc)
    
    def __repr__(self):
        return self.name + " is a " + self.colorCombination + " permanent spell with a mana cost of " + self.manaCost + " that costs $" + str(self.dollarCost)

class Creature(Permanent):
    def __init__(self, dc, c, n, mc, p, t):
        Spell.__init__(self, dc, c, n, mc)
        self.power = p
        self.toughness = t
    
    def __repr__(self):
        return self.name + " is a " + self.colorCombination + " creature spell with a mana cost of " + self.manaCost + " and stats of " + str(self.power) + "/" + str(self.toughness) + \
            " that costs $" + str(self.dollarCost)
