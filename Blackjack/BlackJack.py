import random
import os
import platform

def clear_terminal():
    # Ermittelt das Betriebssystem
    current_os = platform.system()

    # Löscht das Terminal entsprechend dem Betriebssystem
    if current_os == "Windows":
        os.system('cls')
    else:
        os.system('clear')


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = random.choice(cards)
    return random_card


def calculate_score(l1, l2):
    """ Calculate the score in Lists and returns an int """
    computer_score = sum(l2)
    player_score = sum(l1)

    for card in l1:  # Prüfen ob der Spieler mehr als 22 hat und ein Ass im Stapel
        if card == 11 and player_score > 21:
            l1.remove(card)
            l1.append(1)
    player_score = sum(l1)

    for card in l2:
        if card == 11 and computer_score > 21:
            l2.remove(card)
            l2.append(1)
    computer_score = sum(l2)

    if len(l1) == 2 and len(l2) == 2:
        if player_score == 21:
            player_score = 0
        if computer_score == 21:
            computer_score = 0
    return player_score, computer_score, l1, l2


def compare(p_sum, c_sum, u_cards, c_cards):

    if p_sum > 21:
        print(f"\n You loose!\n\nPlayer Cards: {u_cards} = {p_sum}\nComputer Cards: {c_cards} = {c_sum}")
    elif p_sum == c_sum:
        print(f"\nIts a Draw!\n\nPlayer Card: {u_cards} = {p_sum} \nComputer Cards: {c_cards} = {c_sum} ")
    elif p_sum < c_sum and c_sum >= 17 and c_sum <= 21:
        print(f"\n You loose!\n\nPlayer Cards: {u_cards} = {p_sum}\nComputer Cards: {c_cards} = {c_sum}")
    elif p_sum <= 21 and p_sum > c_sum and c_sum >= 17:
        print(f"\n You Win!\n\nPlayer Cards: {u_cards} = {p_sum}\nComputer Cards: {c_cards} = {c_sum}")
    elif c_sum == 21:
        print(f"\n You loose!\n\nPlayer Cards: {u_cards} = {p_sum}\nComputer Cards: {c_cards} = {c_sum}")
    elif c_sum == 0:
        print(f"\n You loose!\nComputer got BLACKJACK!\n\nPlayer Cards: {u_cards} = {p_sum}\nComputer Cards: {c_cards} = 21")
    elif c_sum > 21:
        print(f"\n You Win!\n\nPlayer Cards: {u_cards} = {p_sum}\nComputer Cards: {c_cards} = {c_sum}")
    elif c_sum > p_sum and c_sum < 21:
        print(f"\n You loose!\n\nPlayer Cards: {u_cards} = {p_sum}\nComputer Cards: {c_cards} = {c_sum}")







def game ():

    computer_sum = 0
    player_sum = 0
    deal_card()
    user_cards = []
    computer_cards = [10,11]


    while len(user_cards) < 2:
        randomcard = deal_card()
        user_cards.append(randomcard)

    while len(computer_cards) < 2:
        randomcard2 = deal_card()
        computer_cards.append(randomcard2)
    play = False
    while not play:
        #Prüfen Auf Blackjack
        player_sum, computer_sum, user_cards, computer_cards = calculate_score(user_cards, computer_cards,)
        if player_sum == 0 and computer_sum == 0:
            print(f"Its a Draw!\n\nPlayer Cards {user_cards}\nComputer Cards {computer_cards}")
            restart = input("\n1You want to restart? 'y' or 'n'").lower()
            if restart == "y":
                clear_terminal()
                game()
            elif restart == "n":
                play = True
        if player_sum == 0:
            print(f"\nPlayer Wins! BLACKJACK\nPlayer Cards{user_cards}\nComputer Cards {computer_cards} = {computer_sum}")
            restart = input("\n2You want to restart? 'y' or 'n'").lower()
            if restart == "y":
                clear_terminal()
                game()
            elif restart == "n":
                play = True
        else:
            print(f"\nPlayer Cards {user_cards} = {player_sum}\nComputer Cards {computer_cards}")
            choose = input("\nDo you want to 'Hit' or 'Stand'? ").lower()
            if choose == "hit":
                randomcard = deal_card()
                user_cards.append(randomcard)
                player_sum, computer_sum, user_cards, computer_cards = calculate_score(user_cards, computer_cards)
                if player_sum > 21:
                    compare(player_sum, computer_sum, user_cards, computer_cards)
                    restart = input("\n3You want to restart? 'y' or 'n'").lower()
                    if restart == "y":
                        clear_terminal()
                        game()
                    elif restart == "n":
                        play = True
            elif choose == "stand":
                if computer_sum == 0:
                    compare(player_sum, computer_sum, user_cards, computer_cards)
                    restart = input("\n4You want to restart? 'y' or 'n'").lower()
                    if restart == "y":
                        clear_terminal()
                        game()
                    elif restart == "n":
                        play = True
                elif computer_sum > player_sum:
                    compare(player_sum, computer_sum, user_cards, computer_cards)
                    restart = input("\n5You want to restart? 'y' or 'n'").lower()
                    if restart == "y":
                        clear_terminal()
                        game()
                    elif restart == "n":
                        play = True
                else:
                    while computer_sum < 17 and computer_sum < player_sum:

                        randomcard2 = deal_card()
                        computer_cards.append(randomcard2)
                        player_sum, computer_sum, user_cards, computer_cards = calculate_score(user_cards, computer_cards)
                    if computer_sum >= 21:
                        compare(player_sum, computer_sum, user_cards, computer_cards)
                        restart = input("\n6You want to restart? 'y' or 'n'").lower()
                        if restart == "y":
                            clear_terminal()
                            game()
                        elif restart == "n":
                            play = True
                    elif computer_sum > player_sum:
                        compare(player_sum, computer_sum, user_cards, computer_cards)

                        restart = input("\n7You want to restart? 'y' or 'n'").lower()
                        if restart == "y":
                            clear_terminal()
                            game()
                        elif restart == "n":
                            play = True
                    else:
                        compare(player_sum, computer_sum, user_cards, computer_cards)
                        restart = input("\n8You want to restart? 'y' or 'n'").lower()
                        if restart == "y":
                            clear_terminal()
                            game()
                        elif restart == "n":
                            play = True

                #if computer_sum > player_sum:
                    #compare(player_sum, computer_sum, user_cards, computer_cards)
                    #restart = input("3You want to restart? 'y' or 'n'").lower()
                    #if restart == "y":
                        #game()
                    #else:
                        #play = True





game()




#  Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of
#  the actual score. 0 will represent a blackjack in our game.

# Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace
#  it with a 1. You might need to look up append() and remove().

# TODO 6: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21,
#  then the game ends.

# TODO 7: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card()
#  function to add another card to the user_cards List. If no, then the game has ended.

# TODO 8: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated
#  until the game ends.

# TODO 9: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as
#  it has a score less than 17.

# TODO 10: Create a function called compare() and pass in the user_score and computer_score. If the computer and user
#  both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user
#  has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score
#  is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

# TODO 11: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game
#  of blackjack and show the logo from art.py.
