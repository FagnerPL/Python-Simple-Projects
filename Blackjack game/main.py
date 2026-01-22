import random
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def blackjack():
    print(art.logo)
    user_cards = random.choices(cards, k=2)
    computer_cards = random.choices(cards, k=2)

    def valid_ace():
        if sum(user_cards) > 21 and cards[0] in user_cards:
            user_cards.remove(11)
            user_cards.append(1)
        if sum(computer_cards) > 21 and cards[0] in computer_cards:
            computer_cards.remove(11)
            computer_cards.append(1)

    def final_hands():
        print(f"Your final hand {user_cards}, final score: {sum(user_cards)}")
        print(f"Computer's final hand {computer_cards}, final score: {sum(computer_cards)}")

    def current_hands():
        print(f"Your cards {user_cards}, current score: {sum(user_cards)}")
        print(f"Computer's cards: {computer_cards}, score: {sum(computer_cards)}\n")

    valid_ace()
    current_hands()

    game_on = True
    if sum(computer_cards) == 21:
        final_hands()
        print("Computer wins with a Blackjack")
        game_on = False
    elif sum(user_cards) == 21:
        final_hands()
        print("Win with a Blackjack 😎")
        game_on = False

    while game_on:
        new_card = input("Type 'y' to get another card, type 'n' to pass: ")
        if new_card == "y":
            user_cards.append(random.choice(cards))
            valid_ace()
            current_hands()
            if sum(user_cards) > 21:
                final_hands()
                print("You went over. You lose 😭\n")
                game_on = False

        elif new_card == "n":
            while sum(computer_cards) < 17:
                computer_cards.append(random.choice(cards))
                valid_ace()
            if sum(computer_cards) > 21:
                final_hands()
                print("Opponent went over. You win 😁\n")
                game_on = False
            else:
                if sum(user_cards) > sum(computer_cards):
                    final_hands()
                    print("You win!\n")
                    game_on = False
                elif sum(user_cards) < sum(computer_cards):
                    final_hands()
                    print("You lose!\n")
                    game_on = False
                else:
                    final_hands()
                    print("Drawn!\n")
                    game_on = False

    if input("Do you want to play a game of Blackjack? Type 'y' or 'n': \n") == "y":
        blackjack()
blackjack()


