from Deck import Deck
from Hand import Hand
from Chips import Chips


def take_bet(chips):
    while True:
        try:
            chips.bet = int(input(f"You have {chips.total}. How much you want to bet?"))
        except ValueError:
            print("Must be integer")
        else:
            if chips.bet > chips.total:
                print("Excedeed total chips ammount")
            else:
                break


def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing

    while True:
        x = input("Hit or Stand?")

        if x.lower() == 'hit' or x.lower() == 'h':
            hit(deck, hand)
        elif x.lower() == 'stand' or x.lower() == 's':
            print("Player Stands")
            playing = False
        else:
            print("Wrong input")
            continue
        break


def show_some(player, dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('', dealer.cards[1])
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =", player.value)


def show_all(player, dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =", dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =", player.value)


def player_busts(player, dealer, chips):
    print("\nPlayer busts!")
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print("\nPlayer wins!")
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print("\nDealer busts!")
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print("\nDealer wins!")
    chips.lose_bet()


def push(player, dealer):
    print("\nDealer and Player tie! It's a push.")


chips = Chips()
end_game = False
sec_deck = []
deck = Deck()
deck.shuffle()

print('Welcome to BlackJack! Get as close to 21 as you can without going over!\n\
    Dealer hits until she reaches 17. Aces count as 1 or 11.\n')

while True:

    playing = True

    if len(deck.deck) < 10:
        for card in sec_deck:
            deck.deck.append(sec_deck.pop())
        deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    take_bet(chips)

    show_some(player_hand, dealer_hand)

    while playing:

        hit_or_stand(deck, player_hand)

        show_some(player_hand, dealer_hand)

        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, chips)
            break
    if player_hand.value <= 21:

        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

    show_all(player_hand, dealer_hand)

    if dealer_hand.value > 21:
        dealer_busts(player_hand, dealer_hand, chips)
    elif dealer_hand.value < player_hand.value <= 21:
        player_wins(player_hand, dealer_hand, chips)
    elif player_hand.value < dealer_hand.value <= 21:
        dealer_wins(player_hand, dealer_hand, chips)
    else:
        push(player_hand, dealer_hand)

    print("\nPlayer's winnings stand at", chips.total)

    while True:
        ask = input("Do you wanna play again? Y/N")

        if ask.lower() == 'y':
            break
        elif ask.lower() == 'n':
            print("Thx 4 game")
            end_game = True
            break
        else:
            print("Wrong decision. Try again")
            continue
    if end_game:
        break

## TODO  deck ends
