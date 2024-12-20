import random

# Define the ranks and suits of a deck of cards
ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

# Define a class for a card
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return f'{self.rank} of {self.suit}'

# Define a class for a deck of cards
class Deck:
    def __init__(self):
        self.cards = [Card(rank, suit) for rank in ranks for suit in suits]
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

# Define a class for a solitaire game
class Solitaire:
    def __init__(self):
        self.deck = Deck()
        self.tableau = [[] for _ in range(7)]
        self.foundation = [[] for _ in range(4)]
        self.stockpile = []

        # Deal the cards to the tableau
        for i in range(7):
            for j in range(i+1):
                self.tableau[i].append(self.deck.deal())

        # Move the top card from each tableau pile to the stockpile
        for pile in self.tableau:
            self.stockpile.append(pile.pop())

    def display_tableau(self):
        for i, pile in enumerate(self.tableau):
            print(f'Pile {i+1}: {pile}')

    def display_foundation(self):
        for i, pile in enumerate(self.foundation):
            print(f'Foundation {i+1}: {pile}')

    def display_stockpile(self):
        print(f'Stockpile: {self.stockpile}')

    def play_card(self, pile_number, card_number):
        pile = self.tableau[pile_number-1]
        if card_number > len(pile):
            print('Invalid card number.')
            return
        card = pile.pop(card_number-1)
        print(f'Playing {card} from pile {pile_number}')

    def move_card(self, from_pile, to_pile, card_number):
        from_pile = self.tableau[from_pile-1]
        to_pile = self.tableau[to_pile-1]
        if card_number > len(from_pile):
            print('Invalid card number.')
            return
        card = from_pile.pop(card_number-1)
        to_pile.append(card)
        print(f'Moving {card} from pile {from_pile} to pile {to_pile}')

    def move_to_foundation(self, pile_number, card_number):
        pile = self.tableau[pile_number-1]
        if card_number > len(pile):
            print('Invalid card number.')
            return
        card = pile.pop(card_number-1)
        for foundation in self.foundation:
            if not foundation or (foundation[-1].rank == 'King' and card.rank == 'Ace') or \
               (ranks.index(card.rank) == ranks.index(foundation[-1].rank) + 1 and \
                card.suit == foundation[-1].suit):
                foundation.append(card)
                print(f'Moving {card} to foundation.')
                return
        print('Cannot move card to foundation.')

    def draw_card(self):
        if self.deck.cards:
            card = self.deck.deal()
            self.stockpile.append(card)
            print(f'Drew {card}.')
        else:
            print('No more cards in deck.')

    def play_game(self):
        while True:
            print('\nTableau:')
            self.display_tableau()
            print('\nFoundation:')
            self.display_foundation()
            print('\nStockpile:')
            self.display_stockpile()
            action = input('\nEnter action (play/move/draw/quit): ')
            if action == 'play':
                pile_number = int(input('Enter pile number: '))
                card_number = int(input('Enter card number: '))
                self.play_card(pile_number, card_number)
            elif action == 'move':
                from_pile = int(input('Enter from pile number: '))
                to_pile = int(input('Enter to pile number: '))
                card_number = int(input('Enter card number: '))
                self.move_card(from_pile, to_pile, card_number)
            elif action == 'draw':
                self.draw_card()
            elif action == 'quit':
                break
            elif action == 'move_to_foundation':
                pile_number = int(input('Enter pile number: '))
                card_number = int(input('Enter card number:
                                self.move_to_foundation(pile_number, card_number)
            else:
                print('Invalid action. Please try again.')

    def check_win(self):
        for foundation in self.foundation:
            if len(foundation) != 13:
                return False
        return True

    def play_game(self):
        while True:
            print('\nTableau:')
            self.display_tableau()
            print('\nFoundation:')
            self.display_foundation()
            print('\nStockpile:')
            self.display_stockpile()
            action = input('\nEnter action (play/move/draw/quit/move_to_foundation/check_win): ')
            if action == 'play':
                pile_number = int(input('Enter pile number: '))
                card_number = int(input('Enter card number: '))
                self.play_card(pile_number, card_number)
            elif action == 'move':
                from_pile = int(input('Enter from pile number: '))
                to_pile = int(input('Enter to pile number: '))
                card_number = int(input('Enter card number: '))
                self.move_card(from_pile, to_pile, card_number)
            elif action == 'draw':
                self.draw_card()
            elif action == 'quit':
                break
            elif action == 'move_to_foundation':
                pile_number = int(input('Enter pile number: '))
                card_number = int(input('Enter card number: '))
                self.move_to_foundation(pile_number, card_number)
            elif action == 'check_win':
                if self.check_win():
                    print('Congratulations, you won!')
                else:
                    print('You have not won yet.')
            else:
                print('Invalid action. Please try again.')

# Create a new solitaire game and play it
game = Solitaire()
game.play_game()
