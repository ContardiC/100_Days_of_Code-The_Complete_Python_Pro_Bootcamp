import random
from art import logo
#  MY VERSION
# def is_black_jack(cards):
#     if len(cards) == 2:
#         if ( cards[0] == 11 and cards[1] == 10 ) or ( cards[0] == 10 and cards[1] == 11):
#             return True
#     return False
# def calculate_score(cards):
#     score = 0
#     for card in cards:
#         score+=card
#     return score
# def ace_value(cards):
#     score = calculate_score(cards)
#     for card in cards:
#         if card == 11:
#             if score > 21:
#                 return score - 10
#         else:
#             return score
# game_over = False
# while not game_over:
#     cards = [ 11, 2, 3, 4, 5, 6, 7 ,8 ,9, 10, 10, 10, 10, 10]
#     user_cards = [cards[random.randint(0, 12)], cards[random.randint(0, 12)]]
#
#     deal_cards = [cards[random.randint(0, 12)], cards[random.randint(0, 12)]]
#     #print(f"Deal cards: {deal_cards} - Score: {calculate_score(deal_cards)}")
#
#     if is_black_jack(deal_cards):
#         print(f"Computer Win")
#     else:
#         if is_black_jack(user_cards):
#             print(f"User Win")
#
#     #print(ace_value(user_cards))
#     print(f"\t Your cards: {user_cards}, current score: {ace_value(user_cards)}")
#     print(f"\t Computer's first cards: {deal_cards[0]}")
#
#     if is_black_jack(deal_cards) or ace_value(user_cards) > 21:
#         print(f"You lose")
#     else:
#         if is_black_jack(user_cards):
#             print(f"You win")
#     another_card = True
#     while another_card:
#         choice = input("Type 'y' to get another card, type 'n' to pass: ")
#         if choice == 'n':
#             another_card = False
#             while ace_value(deal_cards) < 17:
#                 deal_cards.append(random.randint(0, 12))
#             print(f"\t Your final hand: {user_cards}, final score: {ace_value(user_cards)}")
#             print(f"\t Computer's final hand: {deal_cards}, final score: {ace_value(deal_cards)}")
#             if ace_value(user_cards) > ace_value(deal_cards):
#                 print("You win")
#                 game_over = True
#             elif ace_value(user_cards) < ace_value(deal_cards):
#                 print("You lose")
#                 game_over = True
#             else:
#                 print("Draw")
#                 game_over = True
#         else:
#             user_cards.append(random.randint(0,12))
#             print(f"\t  Your cards: {user_cards}, current score: {ace_value(user_cards)}")
#             print(f"\t  Computer's first cards: {deal_cards[0]}")
#             if ace_value(user_cards)>21:
#                 print(f"\t Your final hand: {user_cards}, final score: {ace_value(user_cards)}")
#                 print(f"\t Computer's final hand: {deal_cards}, final score: {ace_value(deal_cards)}")
#                 print("You lose")
#                 another_card=False
#                 game_over = True
#     if game_over:
#         c=input("Another game? 'y' for yes 'n' for no")
#         if c == "n":
#             game_over=True
#         else:
#             game_over=False
#             print("\n"*50)

# COURSE VERSION

def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards)==21 and len(cards) ==2:
        return 0 # per indicare che è black jack
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw 🙃"
    elif c_score == 0: # blackjack
        return "Lose, opponent has Blackjack 😱"
    elif u_score == 0:
        return "Win with a Blackjack 😎"
    elif u_score > 21:
        return "You went over. You lose 😭"
    elif c_score > 21:
        return "Opponent went over. You win 😬"
    elif u_score > c_score:
        return "You win 😀"
    else:
        return "You lose 😤"

def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False
    # quando non mi serve una variabile per il loop posse usare underscore _
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first cards: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score !=0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n"*20)
    play_game()