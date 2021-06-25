class Hand:

    def __init__(self, name):
        self.name = name
        self.cards = []

    def collect_card(self, card):
        self.cards.append(card)

    def play_card(self, card_index):
        return self.cards.pop(card_index)

    def share_card(self, deck, player_hand, play_deck):
        while True:
            try:
                while True:
                    no_of_cards = int(input('How many cards do you want to share? '))
                    if no_of_cards <= 26:
                        break
                    else:
                        print("Sorry the limit is 26 cards")
            except ValueError:
                print('Enter a digit!')
            else:
                for _ in range(no_of_cards):
                    player_hand.collect_card(deck.deal())
                    self.collect_card(deck.deal())
                card = deck.deal()
                play_deck.add_card(card)
                if card.value == 20:
                    play_deck.add_card(card)
                break

    def print_cards(self):
        if len(self.cards) == 1:
            print(f'{self.name} card is: ')
        else:
            print(f'{self.name} cards are: ')
        card_index = 0
        for card in self.cards:
            print(f'\t  {card}        Card_Index = {card_index}')
            card_index += 1
