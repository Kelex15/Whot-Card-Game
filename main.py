from deck import Deck, PlayDeck
from card import Card
from hand import Hand
from game_data import suits


def start_game():
    """

    :return: True if the player choice is yes returns false otherwise
    """
    again = False
    while not again:
        choice = input('Do you want to start playing? Yes or No: ')

        if len(choice) > 0 and choice.capitalize()[0] == 'Y':
            return True
        elif len(choice) > 0 and choice.capitalize()[0] == 'N':
            again = True
        else:
            print('Invalid choice!! Try again')

    return False


def card_index():
    """

    :return: The player's index choice
    """
    while True:
        try:
            index_ = int(input('Enter the card index of the card you want to play: '))
        except ValueError:
            print('Enter a digit!')
        else:
            return index_


def play_or_market():
    """

    :return: The choice of the player
    """
    while True:
        choice = input(
            "\nDo you want to go to market(M) or play(P)? (Enter 'q' if you want to quit)").capitalize()

        if len(choice) > 0 and choice[0] == 'M':
            return choice[0]

        elif len(choice) > 0 and choice[0] == 'P':
            return choice[0]
        elif len(choice) > 0 and choice[0] == 'Q':
            while True:
                quit_game = input('Do you want to quit? y or n ').lower()
                if quit_game == 'y':
                    return quit_game
                elif quit_game == 'n':
                    break
                else:
                    print('Invalid choice')
        else:
            print('Invalid choice')


def special_card(card_rank):
    """

    :param card_rank:
    :return: True if the card rank is special returns False otherwise
    """
    if card_rank == '1' or card_rank == '2' or card_rank == '14' or card_rank == '20':
        return True
    return False


def whot_card():
    """

    :return: The suit of the card wanted
    """
    while True:
        wanted_card = input('What card do you want? ').capitalize()

        if wanted_card not in suits:
            print('\nCard not recognized!')
        else:
            print(f'\nI need: {wanted_card}')
            break
    return wanted_card


def perform_function(hand_name, card_rank, hand):
    """

    :param hand_name:
    :param card_rank:
    :param hand:
    :return: True if the special card rank is 1 else perform the function of the special card and return False
    """
    if card_rank == '1':
        print('Hold On!')
        return True
    elif card_rank == '2':
        print('Pick Two!')
        for i in range(2):
            if len(deck.all_cards) == 0:
                break
            else:
                hand.collect_card(deck.deal())
    elif card_rank == '14':
        print('Go Gen!')
        hand.collect_card(deck.deal())
    elif card_rank == '20':
        if hand_name.capitalize() == "Player":
            suit_requested = whot_card()
            play_deck.add_card(Card(suit_requested, '0'))
        else:
            main_card = 0
            for c in dealer_hand.cards:
                if c.rank != '20':
                    main_card = c
                    break
            suit_requested = main_card.suit
            play_deck.add_card(Card(suit_requested, '0'))

    return False


def win_check(player_cards, dealer_cards):
    """
    Check if the player or dealer has won
    :param player_cards:
    :param dealer_cards:
    :return:
    """
    sum_of_player_cards = 0
    sum_of_dealer_cards = 0

    for c in player_cards:
        sum_of_player_cards += c.value
    for c in dealer_cards:
        sum_of_dealer_cards += c.value

    print('\n')
    if sum_of_dealer_cards < sum_of_player_cards:
        print('You Lose!!       :(')
    elif sum_of_dealer_cards > sum_of_player_cards:
        print('You Win!!       :)')
    else:
        print('It\'s a tie')


def play_again():
    """

    :return: True if player choice is Yes returns False otherwise
    """
    again = False
    while not again:
        choice = input('Do you want to play again? Y or N: ')

        if len(choice) > 0 and choice.capitalize()[0] == 'Y':
            return True
        elif len(choice) > 0 and choice.capitalize()[0] == 'N':
            again = True
        else:
            print('Invalid choice!! Try again')

    return False


#  MAIN GAME LOGIC
print('O--O----WELCOME TO WHOT CARD GAME!----O--O')
print('\n')
start = start_game()
while start:
    print('\n')

    quit_ = False

    deck = Deck()
    play_deck = PlayDeck()
    deck.shuffle()
    player_hand = Hand('Kelex')
    dealer_hand = Hand('Dealer')

    dealer_hand.share_card(deck, player_hand, play_deck)
    print('\n')

    player_hold = 0
    while len(deck.all_cards) != 0:
        if len(player_hand.cards) == 0:
            break
        elif len(dealer_hand.cards) == 0:
            break

        else:
            play_deck.print_card()
            dealer_turn = True
            if player_hold == 0:
                player_turn = True
            else:
                player_turn = False

            while player_turn:
                print('\n')
                print('Your turn:')
                player_hand.print_cards()
                player_choice = play_or_market()
                if player_choice == 'M':
                    player_hand.collect_card(deck.deal())
                    player_turn = False
                    print('\n')
                    play_deck.print_card()
                elif player_choice == 'y':
                    quit_ = True
                    break
                else:
                    while True:
                        player_card_index = card_index()
                        if player_card_index >= len(player_hand.cards) or player_card_index < 0:
                            print('Index not available! Try again!')
                        else:
                            break
                    player_card = player_hand.play_card(player_card_index)
                    if player_card.suit == play_deck.card().suit or player_card.rank == play_deck.card().rank\
                            or player_card.rank == '20':
                        play_deck.add_card(player_card)
                        if special_card(player_card.rank):
                            print("\n")
                            result = perform_function("Player", player_card.rank, dealer_hand)
                            dealer_turn = not result
                        player_turn = False
                    else:
                        print('Card does not match!')
                        player_hand.collect_card(player_card)
                    print('\n')
                    play_deck.print_card()

            if quit_:
                break

            if player_hold == 1:
                player_hold -= 1

            if len(deck.all_cards) == 0:
                break

            if len(player_hand.cards) == 0:
                break

            print('\n')
            while dealer_turn:
                print('Dealer\'s turn: ')
                dealer_card = 0
                index = 0
                for card in dealer_hand.cards:
                    if card.suit == play_deck.card().suit:
                        played_card = dealer_hand.play_card(index)
                        dealer_card = played_card
                        break
                    elif card.rank == play_deck.card().rank:
                        played_card = dealer_hand.play_card(index)
                        dealer_card = played_card
                        break
                    elif card.rank == '20':
                        played_card = dealer_hand.play_card(index)
                        dealer_card = played_card
                        break
                    index += 1

                if dealer_card == 0:
                    print('Dealer went to market!')
                    print('\n')
                    dealer_hand.collect_card(deck.deal())
                    dealer_turn = False
                else:
                    play_deck.add_card(dealer_card)
                    print(f'Dealer played {dealer_card}\n')
                    dealer_turn = False
                    if special_card(dealer_card.rank):
                        result = perform_function("Dealer", dealer_card.rank, player_hand)
                        if result:
                            player_hold += 1
                    if len(dealer_hand.cards) == 1:
                        print('Dealer: Last card!\n')
                    if len(dealer_hand.cards) == 0:
                        print('Dealer: Check up!\n')

            for _ in range(20, -1, -5):
                if len(deck.all_cards) == _:
                    print(f"\nThere are {_} cards remaining in the deck")

    if quit_:
        break
    if len(deck.all_cards) == 0:
        print("The cards in the deck is finished")
    win_check(player_hand.cards, dealer_hand.cards)
    if len(player_hand.cards) != 0:
        player_hand.print_cards()
        print("\n")
    if len(dealer_hand.cards) != 0:
        dealer_hand.print_cards()

    if not play_again():
        break

print('\n')
print('Thanks for playing \nGoodbye :)')
