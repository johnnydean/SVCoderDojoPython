ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]

class Card:
    def __init__(self, rankID, suitID):
        self.suitID = suitID
        self.rankID = rankID
        self.rank = ranks[rankID-1]
        self.suit = suits[suitID-1]



myCard = Card(13,3)

print myCard.rank
print myCard.suit

print "Now we're making another card"

myOtherCard = Card(2,3)

print myOtherCard.rank
print myOtherCard.suit

print "Now we're making a deck"

deck = []
for rank in range(1,14):
    for suit in range(1,5):
        deck.append(Card(rank,suit))
