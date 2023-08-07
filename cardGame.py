class Card:
    def __init__(self, cost, color):
        self.color = color
        self.cost = cost

class Player:
    def __init__(self, gems, cards = {}):
        pass

    def can_purchase(self, card):
        for color in card.items():
            if card.cost[color] - self.cards[color] > self.gems[color]:
                return False
        
        return True

    def purchase(self, card):
        if self.can_purchase(card):
            for color in card.cost.items():
                self.gems = self.gems - card.cost[color] + self.cards[color]
            
            self.cards[card.color] = self.cards[card.color] + 1

        return True