from typing import Dict


class Card:
    VALUES: Dict[str, int] = {
        '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
        '7': 7, '8': 8, '9': 9, '10': 10,
        'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11
    }
    SUITS = ['♣', '♦', '♥', '♠']

    def __init__(self, rank: str, suit: str) -> None:
        """
        Initialize a new Card instance.

        Args:
            rank (str): The rank of the card, e.g., '2', '3', 'Ace'.
            suit (str): The suit of the card, one of ['♣', '♦', '♥', '♠'].

        Raises:
            ValueError: If rank or suit is not valid.
        """
        if rank not in self.VALUES:
            raise ValueError("Invalid card rank!")
        if suit not in self.SUITS:
            raise ValueError("Invalid card suit.")

        self._rank = rank
        self._suit = suit

    @property
    def rank(self) -> str:
        """
        Retrieve the rank of the card.

        Returns:
            str: The rank of the card.
        """
        return self._rank

    @property
    def suit(self) -> str:
        """
        Retrieve the suit of the card.

        Returns:
            str: The suit of the card.
        """
        return self._suit

    @property
    def value(self) -> int:
        """
        Retrieve the numeric value of the card based on its rank.

        Returns:
            int: The numeric value of the card.
        """
        return self.VALUES[self._rank]

    def __repr__(self) -> str:
        """
        String representation of the card in the format 'Rank of Suit'.

        Returns:
            str: String representation of the card.
        """
        return f"{self.rank} of {self.suit}"
