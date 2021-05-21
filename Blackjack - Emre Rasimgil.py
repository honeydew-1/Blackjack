import random

ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
suits = ['♣', '♦', '♥', '♠']
vals = {'Ace': 1, '2': 2, '3': 3, '4': 4, '5': 5, 
        '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 
        'Jack': 10, 'Queen': 10, 'King': 10 }

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
 
    def set_val(self):
        return vals[self.rank]
    
    def __repr__(self):
        return f"{self.rank} of {self.suit}"
    
    def getRank(self):
        return self.rank
        
class Deck:
    def __init__(self):
        self.d = [Card(rank, suit) for rank in ranks for suit in suits]
        random.shuffle(self.d)
 
    def draw(self):
        return self.d.pop()

class Hand:
    def __init__(self):
        self.hand = []
        self.total = 0
        self.ace = False
    
    def hit(self, card_num):
        for _ in range(card_num):
            card = deck.draw()
            self.hand.append(card)
            if card.rank == 'Ace': self.ace = True 
            self.total += card.set_val()
            if self.ace and self.total < 12: self.total += 10
 
    def __repr__(self):
        t = ', '
        return f'{t.join(map(str,self.hand))} || Total: {self.total}'
    
    def toList(self):
        return self.hand
     
class Player:
    def __init__(self):
        self.hand = Hand()
        self.bank = 100
        self.bet = 0
        self.stand = False
        self.hit = False
        self.blackjack = False
        self.pairs = False
        self.ladies = False
        self.under = False
        self.over = False

    def makeBet(self, x):
        self.bet += x
        self.bank -= x
        return self.bet, self.bank

class Dealer:
    def __init__(self):
        self.hand = Hand()

deck = Deck()
player = Player()
dealer = Dealer()

def sideBet():
    global sideBetAmount
    d = input("Would you like to place side bet? Y/N ")
    print()
    
    if d.upper() == 'Y':
        sideBetAmount = int(input('How much would you like to bet? $'))
        print()
        if sideBetAmount > player.bank:
            while sideBetAmount > player.bank:
                print('Not enough cash.\n')
                sideBetAmount = int(input('How much would you like to bet? $'))
                print()
        player.bank -= sideBetAmount
        sideBetsList = ['(i) Lucky Ladies', '(ii) Perfect Pairs', '(iii) O/U 13.5']
        print(*sideBetsList)
        print()
        placedSideBet = input('Please choose a side bet. ')
        print()
        if placedSideBet.upper() == 'I' or placedSideBet == '1': player.ladies = True
        if placedSideBet.upper() == 'II' or placedSideBet == '2': player.pairs = True
        if placedSideBet.upper() == 'III' or placedSideBet == '3': 
            overUnder = input('O/U? ')
            print()
            if overUnder.upper() == 'O':player.over = True
            if overUnder.upper() == 'U':player.under = True

def luckyLadies():
        if player.hand.total == 20: 
            player.bank += sideBetAmount * 4
            print(f'Your side bet won! You won {sideBetAmount*4}!\n')
        else: print('Your side bet has lost.\n')
                        
def overUnder():
    if (player.over and player.hand.total > 13) or (player.under and player.hand.total < 13):
        player.bank += 2*sideBetAmount
        print(f'Your side bet won! You won {sideBetAmount*2}!\n')
    if (player.over and player.hand.total < 13) or (player.under and player.hand.total > 13): print('Your side bet has lost.\n')

def perfectPairs():
        c1 = player.hand.toList()[0]
        c2 = player.hand.toList()[1]
        if (c1.getRank() == c2.getRank()): 
            player.bank += sideBetAmount * 5
            print(f'Your side bet won! You won {sideBetAmount*5}!\n')
        if c1.getRank() != c2.getRank(): print('Your side bet has lost.\n')

def sideBetWinner():
    if player.ladies: luckyLadies()
    if player.over or player.under: overUnder()
    if player.pairs: perfectPairs()
    
def hit(hand):
    hand.hit(1)
    print(f'Your hand: {hand}\n')
    while not player.stand and hand.total < 21:
        d = input("(H)it/(S)tand? ")
        print()
        if d.upper() == 'S': player.stand = True
        if d.upper() == 'H':hit(hand)

def resetGame():
    global deck
    player.hand = Hand()
    dealer.hand = Hand()
    player.stand = False
    player.double = False
    player.blackjack = False
    player.ladies = False
    player.pairs = False
    player.under = False
    player.over = False
    deck = Deck()

def playersTurn():
    global bet
    d = input("(H)it/(S)tand/(D)ouble Down? ")
    print()
    if d.upper() == 'D':
        if bet > player.bank:
            while d.upper() == 'D' and bet > player.bank:
                print('Not enough cash to double down.\n')
                d = input("(H)it/(S)tand? ")
                print()
        if player.bank > bet:
            player.bank += bet
            bet *= 2
            player.bank -= bet
            player.hand.hit(1)
            print(f'Your hand: {player.hand}\n')
            if player.hand.total > 21: print(f'Bust! You lost ${bet}!\n')
            player.stand = True
        
    if d.upper() == 'S': player.stand = True
        
    if d.upper() == 'H': hit(player.hand)
                  
    if player.hand.total == 21: player.stand = True 
    if player.hand.total > 21: print(f'Bust! You lost ${bet}!\n')

def dealersTurn():
    global bet
    dealer.hand.hit(1)
    print(f"Dealer's hand: {dealer.hand}\n")
    def pay():
        blackjackBet = bet * 6 // 5
        if player.blackjack == True: payout = blackjackBet + bet
        else: payout = 2 * bet
        print(f'You won ${payout}!\n')
        player.bank += payout
        
    if 21 >= dealer.hand.total >= 17: 
        if dealer.hand.total == player.hand.total: 
            print('Push!\n')
            player.bank += bet
                
        if dealer.hand.total > player.hand.total: print(f'Dealer won! You lost ${bet}!\n')
                
        if (dealer.hand.total < player.hand.total) or (player.hand.total == 21 and dealer.hand.total != 21): pay()
        
    if dealer.hand.total > 21: pay()

def game():
    global bet
    while player.bank > 0:
        print(f'||Bank: ${player.bank}||\n')
        bet = int(input('Choose bet: $'))
        print()
        while bet > player.bank:
            print(f"Not enough cash, can't bet ${bet}")
            print()
            bet = int(input('Choose bet: $'))
            print()
        player.makeBet(bet)
        if player.bank > 0: sideBet()
        player.hand.hit(2)
        print(f'Your hand: {player.hand}\n')
        sideBetWinner()
        dealer.hand.hit(1)
        print(f"Dealer's hand: X, {dealer.hand}\n")
        if player.hand.total == 21:
            player.stand = True
            player.blackjack = True
        
        while player.hand.total < 21 and not player.stand: playersTurn()

        while player.stand and dealer.hand.total <= 16 and player.hand.total <= 21: dealersTurn()
        
        resetGame()
    
    if player.bank == 0: input('Better luck next time!')

game()