from typing import List

from .card import Card


class Hand:
    def __init__(self) -> None:
        """
        Initialize an empty Hand instance.
        """
        self.cards: List[Card] = []

    def add_card(self, card: Card) -> None:
        """
        Add a card to the hand.

        Args:
            card (Card): The card to be added to the hand.
        """
        self.cards.append(card)

    def clear(self) -> None:
        """
        Remove all cards from the hand, thereby clearing it.
        """
        self.cards = []

    @property
    def value(self) -> int:
        """
        Compute the numeric value of the hand, considering the flexibility of the Ace (either 1 or 11).

        Returns:
            int: The calculated numeric value of the hand.
        """
        val = sum(card.value for card in self.cards)
        aces = sum(1 for card in self.cards if card.rank == 'Ace')

        while val > 21 and aces:
            val -= 10
            aces -= 1

        return val

    @property
    def is_bust(self) -> bool:
        """
        Determine if the hand value exceeds 21.

        Returns:
            bool: True if the hand value is greater than 21, otherwise False.
        """
        return self.value > 21

    @property
    def has_blackjack(self) -> bool:
        """
        Check if the hand is a blackjack, which is defined as having an Ace and a 10-value card.

        Returns:
            bool: True if the hand is a blackjack, otherwise False.
        """
        return len(self.cards) == 2 and self.value == 21

    def __str__(self) -> str:
        """
        String representation of the hand.

        Returns:
            str: A comma-separated list of the cards in the hand.
        """
        return ", ".join(map(str, self.cards))

    def __repr__(self) -> str:
        """
        Formal string representation of the hand.

        Returns:
            str: Representation in the format "Hand({list of cards})".
        """
        return f"Hand({self.__str__()})"
