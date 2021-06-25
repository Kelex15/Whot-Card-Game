from game_data import suits, ranks
import random
from card import Card


class Deck:
    """
    A deck of cards that starts out with 54 card objects

    Attributes:
         all_cards: This is a list of all the cards in the deck class
    Methods:
        shuffle: Shuffles all the cards in the all_cards list
        deal: Removes a card object from the first index of the all_cards list and returns it
    """

    def __init__(self):
        self.all_cards = []
        # create a separate list for the suits that dont have the same number of ranks
        star_rank_list = ['1', '2', '3', '4', '5', '6', '7', '8']
        whot_list = ['20']
        not_cross_and_square_rank_list = ['4', '8', '12']
        for suit in suits:
            for rank in ranks:
                if suit == 'Star':
                    if rank in star_rank_list and rank not in whot_list:
                        self.all_cards.append(Card(suit, rank))
                elif suit == 'Cross' or suit == 'Square':
                    if rank not in not_cross_and_square_rank_list and rank not in whot_list:
                        self.all_cards.append(Card(suit, rank))
                elif suit == 'Whot':
                    if rank in whot_list:
                        for i in range(5):
                            self.all_cards.append(Card(suit, rank))
                else:
                    if rank not in whot_list:
                        self.all_cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal(self):
        return self.all_cards.pop(0)


class PlayDeck:

    def __init__(self):
        self.play_deck = []

    def add_card(self, card):
        self.play_deck.insert(0, card)

    def card(self):
        return self.play_deck[0]

    def print_card(self):
        print(f'Play Deck: {self.play_deck[0]}')
