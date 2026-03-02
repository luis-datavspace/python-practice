from art import logo
from random import choice

# Both players (computer and user) will start with two cards.
# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The Ace can count as 11 or 1.
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn and the computer is the dealer.




def deal_cards():
    """Deal the card from the deck"""

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = choice(cards)
    return card

def calculate_score(cards):
    """Check if there is a blackjack in the first deal of cards,
    also check if the ace should count as 11 or 1 depending on whether the group of cards has a higher score than allowed"""

    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(computer_score , user_score):

    if computer_score == user_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "You lose, Opponent has a blackjack"
    elif user_score == 0:
        return "Win with a blackjack"
    elif user_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "Opponent went over. You win"
    elif user_score > computer_score:
        return "You win"
    else:
        return  "You lose"

def blackjack():
    print(logo)

    player_score = -1
    pc_score = -1
    player_cards = []
    computer_cards = []

    for i in range(2):

        player_cards.append(deal_cards())
        computer_cards.append(deal_cards())
    game_over = False

    while not game_over:

        player_score = calculate_score(player_cards)
        pc_score = calculate_score(computer_cards)
        print(f"Your cards: {player_cards}, current score: {player_score}\nComputer's first card: {computer_cards[0]}")

        if (pc_score or player_score) == 0 or player_score > 21:
            game_over = True

        else:
            should_continue = input("Type 'y' to get another card, type 'n' to pass: ").lower()

            if should_continue == 'y':
                player_cards.append(deal_cards())
            else:
                game_over = True

    while pc_score < 17 and pc_score != 0:
        computer_cards.append(deal_cards())
        pc_score = calculate_score(computer_cards)

    print(f"Your final hand: {player_cards}, final score: {player_score}\nComputer's final hand: {computer_cards}, final score: {pc_score}")
    print(compare(pc_score,player_score))



while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
    print("\n" * 20)
    blackjack()

print("\nGoodBye!\n")