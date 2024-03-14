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

By Matthew F