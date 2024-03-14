class Card:
    def __init__(self, dc, n):
        self.dollarCost = dc
        self.name = n
        
    def __repr__(self):
        return self.name + "costs $" + str(self.dollarCost)

    def __add__(self, other):
        return "It costs $" + str(self.dollarCost + other.dollarCost) + " to buy both " + self.name + " and " + other.name

    def __sub__(self, other):
        if self.dollarCost > other.dollarCost:
            return self.name + " costs $" + str(round(self.dollarCost - other.dollarCost, 2)) + " more than " + other.name
        elif self.dollarCost < other.dollarCost:
            return other.name + " costs $" + str(round(other.dollarCost - self.dollarCost, 2)) + " more than " + self.name
        else:
            return self.name + " and " + other.name + " both cost $" + str(self.dollarCost)

class Land(Card):
    def __init__(self, dc, mp, n):
        Card.__init__(self, dc, n)
        self.manaProduced = mp

    def __repr__(self):
        return self.name + " is a land that taps for " + self.manaProduced + " and costs $" + str(self.dollarCost)

class Spell(Card):
    def __init__(self, dc, c, n, mc):
        Card.__init__(self, dc, n)
        self.colorCombination = c
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
bestCard = Creature(0.35, "green", "Colossal Dreadmaw", "4GG", 6, 6)
print(bestCard)
s1 = Spell(3.58, "black", "Murder", "1BB")
l1 = Land(0.05, "B", "Swamp")
p1 = Permanent(0.99, "white", "Pacifism", "1W")
m1 = Card(0.57, "Backup Plan")
print(bestCard+s1)
print(m1-l1)