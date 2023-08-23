import random
from typing import List, Union
from .card import Card


class Deck:
    RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    SUITS = ['♣', '♦', '♥', '♠']

    def __init__(self) -> None:
        """
        Initialize a new Deck instance.

        The deck is constructed with a standard set of 52 cards, each representing a combination of rank and suit.
        The deck is then shuffled.
        """
        self.cards: List[Card] = [Card(rank, suit) for rank in self.RANKS for suit in self.SUITS]
        self.shuffle()

    def shuffle(self) -> None:
        """
        Shuffle the deck of cards.

        Raises:
            ValueError: If the deck is empty.
        """
        if not self.cards:
            raise ValueError("Deck is empty. Cannot shuffle.")
        random.shuffle(self.cards)

    def draw(self) -> Union[Card, None]:
        """
        Draw the top card from the deck.

        Returns:
            Card: The top card of the deck if it is not empty.
            None: If the deck is empty.
        """
        return self.cards.pop() if self.cards else None

    def __len__(self) -> int:
        """
        Retrieve the number of cards left in the deck.

        Returns:
            int: The number of cards remaining in the deck.
        """
        return len(self.cards)

    def __repr__(self) -> str:
        """
        String representation of the deck.

        Returns:
            str: A string in the format "Deck of {number of cards} cards".
        """
        return f"Deck of {len(self)} cards"
