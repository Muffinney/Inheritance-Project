# Inheritance Project Version 1.0
This is a nongraphical application that compares the pricess of different Magic the Gathering cards with classes and subclasses

### How to create a new object

##### Lands
```
l1 = Land(#Monetary cost, #The type of mana the land produces, #Card name)
```

##### Nonpermanent Spells
```
s1 = Spell(#Monetary cost, #Color Combination, #Card name, #Mana Cost)
```

##### Noncreature Permanents
```
p1 = Permanent(#Monetary cost, #Color Combination, #Card name, #Mana Cost)
```

##### Creatures
```
c1 = Creature(#Monetary cost, #Color Combination, #Card name, #Mana Cost, #Power, #Toughness)
```

### How to print your object
```
print(l1)
```

### How to compare monetary costs
Adding prices:
```
print(l1+s1)
```

Difference of prices:
```
print(l1-s1)
```

### Example
```
bestCard = Creature(0.35, "green", "Colossal Dreadmaw", "4GG", 6, 6)
print(bestCard)
```
This outputs "Colossal Dreadmaw is a green creature spell with a mana cost of 4GG and stats of 6/6 that costs $0.35"

By Matthew F