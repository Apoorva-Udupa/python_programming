#Python Program to Shuffle Deck of Cards -  creating cartesian products 
import itertools, random
deck = list(itertools.product(range(1,14),['heart','spade','diamond','club']))
random.shuffle(deck)
print(deck)
#drawing 5 cards
for i in range(0,5):
    print(deck[i][0],'of',deck[i][1])
