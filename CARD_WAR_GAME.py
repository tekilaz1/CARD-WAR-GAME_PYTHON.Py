import math
import copy
import random
print("\n")
print("///////----------WELCOME TO WAR------------//////////")
print("----SOME RULES OF THE GAME----")
print("* you cannot bet more than $50 in a single game")
print("*you can play this game twice before restarting the game")
print("* The inputs to the game described at any point so PAY ATTENTION ")
print("\n")
print("-----GOOD LUCK IN THE CARD GAME----")
bet = 50
bet1 = 50
bet2 = 50
bet3 = 50

def card_game():
    global bet
    global bet1
    player = input("Please enter Name of FIRST player?")
    bet = bet
    print("hello", player, "you currently have",  bet, "dollars")
    print("\n")

    player1 = input("Please enter Name of SECOND player?")
    bet1 = bet

    bet_curr = int(input("please enter your bet amount ( 1- 50 $)"))

    if bet_curr < 1 or bet_curr > 50:
        print("I said between 1 - 50 and you typed", bet_curr)
        print("I don't play with liars!!! BYE")
        exit()
    else:
        print("running the game")
    print("\n")

    if bet <= 0:
        print("you don't have anything to bet. BYE!!")
        exit()

    card1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    suit = ["\u2666", "\u2666", "\u2665", "\u2663"]

    player_hand = copy.copy(card1)
    random.shuffle(player_hand)
    player_hand = random.choice(player_hand)
    player1_hand = copy.copy(card1)
    random.shuffle(player1_hand)
    player1_hand = random.choice(player1_hand)

    A = random.choice(suit)
    random.shuffle(suit)
    B = random.choice(suit)

    if player_hand > player1_hand:
        print("GREAT", player, "your card is", str(player_hand) + A, "and", player1, "card is", str(player1_hand) + B)
        print("you Won the game and $", bet_curr, "have added to your account")
        print("your current account is", bet + bet_curr)
        bet = bet + bet_curr
        bet1 = bet1 - bet_curr
    elif player_hand == player1_hand:
        card_game()

    else:
        print("OPPS", player, "your card is", str(player_hand) + A, "and", player1, "card is", str(player1_hand) + B)
        print("you Lost the game and $", bet_curr, "have reduced from your account")
        print("your current account is", bet - bet_curr)
        bet = bet - bet_curr
        bet1 = bet1 + bet_curr


print("\n")


def card_game2():
    global bet
    global bet1
    global bet2
    global bet3
    player2 = str(input("Please enter your Name?"))
    bet = bet
    print("hello", player2, "you currently have", bet, "dollars")
    print("\n")

    player3 = "computer"
    bet1 = bet1

    bet_curr2 = int(input("please enter your bet amount ( 1- 50 $)"))

    if bet_curr2 < 1 or bet_curr2 > 50:
        print("I said between 1 - 50 and you typed", bet_curr2)
        print("I don't play with liars!!! BYE")
        exit()
    else:
        print("running the game")
        print("\n")

    card1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    suit = ["\u2666", "\u2666", "\u2665", "\u2663"]

    player2_hand = copy.copy(card1)
    random.shuffle(player2_hand)
    player2_hand = random.choice(player2_hand)
    player3_hand = copy.copy(card1)
    random.shuffle(player3_hand)
    player3_hand = random.choice(player3_hand)

    C = random.choice(suit)
    random.shuffle(suit)
    D = random.choice(suit)

    if player2_hand > player3_hand:
        print("GREAT", player2, "your card is", str(player2_hand) + C, "and", player3, "card is", str(player3_hand) + D)
        print("you Won the game and $", bet_curr2, "have added to your account")
        print("your current account is", bet2 + bet_curr2)
        bet2 = bet2 + bet_curr2
        bet3 = bet3 - bet_curr2
    elif player2_hand == player3_hand:
        card_game2()
    else:
        print("OPPS", player2, "your card is", str(player2_hand) + C, "and", player3, "card is", str(player3_hand) + D)
        print("you Lost the game and $", bet_curr2, "have reduced from your account")
        print("your current account is", bet2 - bet_curr2)
        bet2 = bet2 - bet_curr2
        bet3 = bet3 + bet_curr2


print("\n")


def game_choice():
    choice = str(input("Do you want to play with the computer or friend, enter(c  for computer, f for friend?"))
    print("\n")
    global bet
    global bet1
    global bet2
    global bet3
    if choice == "f":
        if bet <= 0:
            print("you don't have anything to bet. BYE!!")
            exit()
        else:
            card_game()

    elif choice == "c":
        if bet2 <= 0:
            print("you don't have anything to bet. BYE!!")
            exit()
        else:
            card_game2()

    else:
        print("please enter a valid  alphabet, either c for computer and f for friend (c or f)")
        exit()


game_choice()
print("\n")


def re_match():

    rematch = input("Do you want to replay the game(yes or no)?")
    if rematch == "yes":
        game_choice()
    else:
        print("Good Bye, See you next Time!!!")


re_match()
