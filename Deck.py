import numpy.rand as r

class Deck:
    cards = []
    
    def draw(self, count = -1):
        if count == -1:
            return self.cards.pop()
        else:
            ret = []
            for i in range(count):
                ret += self.draw()
            return ret
    
    def take_bottom_card(self):
        return self.cards.pop(0)
    
    def add_card_to_top(self, card):
        self.cards.append(card)
    
    def add_card_to_bottom(self, card):
        self.cards.insert(0, card)
    
    def shuffle(self):
        for i in range(len(self.cards)):
            swap_index = r.range(0,len(self.cards))
            temp = self.cards[i]
            self.cards[i] = self.cards[swap_index]
            self.cards[swap_index] = temp