from game.deck import Deck
from game.participant import Dealer, Player

if __name__ == "__main__":
    deck = Deck()
    dealer = Dealer(deck)
    player = Player()

    while True:
        dealer.clear_hand()
        player.clear_hand()

        for _ in range(2):
            dealer.deal(dealer)
            dealer.deal(player)

        print(f"Dealer's face-up card: {dealer.show_card()}")
        print(f"Your hand: {player}")

        if player.hand.has_blackjack:
            print("You have a blackjack!")
            dealer.play_turn()
            if dealer.hand.has_blackjack:
                print("Both you and the dealer have a blackjack! It's a tie!")
                continue
            else:
                print("You win with a blackjack!")
                continue

        while not player.is_bust:
            move = player.decide_move()
            if move == "hit":
                dealer.deal(player)
                print(f"Your hand: {player}")
                if player.is_bust:
                    print("You went bust!")
                    break
            else:
                break

        if not player.is_bust:
            dealer.play_turn()
            print(f"Dealer's hand: {dealer}")

            if dealer.is_bust:
                print("Dealer went bust! You win!")
            elif dealer.value > player.value:
                print("Dealer wins!")
            elif dealer.value < player.value:
                print("You win!")
            else:
                print("It's a tie!")

        play_again = ""
        while play_again not in ["yes", "no"]:
            play_again = input("Do you want to play again? (yes/no) ").lower().strip()
            if play_again == "no":
                exit()
            elif play_again != "yes":
                print("Invalid input. Please answer with 'yes' or 'no'.")
