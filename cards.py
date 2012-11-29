ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]

class Card:
    def __init__(self, rankID, suitID):
        self.suitID = suitID
        self.rankID = rankID
        self.rank = ranks[rankID-1]
        self.suit = suits[suitID-1]

deck = []
for rank in range(1,14):
    for suit in range(1,5):
        deck.append(Card(rank,suit))

print "The deck has", len(deck), "cards in it."
