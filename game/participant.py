from .card import Card
from .deck import Deck
from .hand import Hand


class Participant:
    def __init__(self) -> None:
        """
        Initialize a Participant instance with an empty hand.
        """
        self.hand = Hand()

    def receive_card(self, card: Card) -> None:
        """
        Add a card to the participant's hand.

        Args:
            card (Card): The card to be added.
        """
        self.hand.add_card(card)

    def clear_hand(self) -> None:
        """
        Remove all cards from the participant's hand.
        """
        self.hand.clear()

    @property
    def value(self) -> int:
        """
        Calculate the numeric value of the participant's hand.

        Returns:
            int: The calculated numeric value.
        """
        return self.hand.value

    @property
    def is_bust(self) -> bool:
        """
        Determine if the hand value exceeds 21.

        Returns:
            bool: True if the hand value is greater than 21, otherwise False.
        """
        return self.hand.is_bust

    def __str__(self) -> str:
        """
        String representation of the participant's hand.

        Returns:
            str: The string representation of the participant's cards.
        """
        return str(self.hand)

    def __repr__(self) -> str:
        """
        Formal string representation of the participant.

        Returns:
            str: Representation in the format "{Class name}({cards in hand})".
        """
        return f"{self.__class__.__name__}({self.__str__()})"


class Dealer(Participant):
    def __init__(self, deck: Deck) -> None:
        """
        Initialize a Dealer instance with a given deck.

        Args:
            deck (Deck): The deck to be used by the dealer.
        """
        super().__init__()
        self.deck = deck

    def deal(self, participant: Participant) -> None:
        """
        Deal a card from the deck to a specified participant.

        Args:
            participant (Participant): The participant to receive the card.
        """
        card = self.deck.draw()
        if card:
            participant.receive_card(card)

    def play_turn(self) -> None:
        """
        Dealer's play strategy: Continuously draw cards until reaching a hand value of 17 or more.
        """
        while self.value < 17 and not self.is_bust:
            self.deal(self)

    def show_card(self) -> str:
        """Reveal the first card of the dealer (faced up).

        Returns:
            str: String representation of the first card, or "No cards" if the dealer has no cards.
        """
        if self.hand.cards:
            return str(self.hand.cards[0])
        return "No cards"


class Player(Participant):
    def decide_move(self) -> str:
        """
        Decide the player's next move based on their choice: either 'hit' to draw another card or 'stand' to keep
        their current hand.

        Note:
            This method prompts the user for their decision.

        Returns:
            str: The decision ('hit' or 'stand') made by the player.
        """
        while True:
            decision = input("Do you want to 'hit' or 'stand'? ").lower()
            if decision in ["hit", "stand"]:
                return decision
            print("Invalid choice. Please choose 'hit' or 'stand'.")
