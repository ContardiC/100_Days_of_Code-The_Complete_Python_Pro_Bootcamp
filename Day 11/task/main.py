import random
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
#             while ace_value(deal_cards) < 16:
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

user_cards = []
computer_cards = []
# quando non mi serve una variabile per il loop posso usare underscore _
for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
