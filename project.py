
import random


class Money():
    """
    Handle the amount of money for betting in the game
    """

    def __init__(self, amount=0):
        self.balance = amount

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if(self.balance < amount):
            print(" -> There is not enough money in your balance\n")
            return -1
        self.balance = self.balance - amount
        return amount

    def getBalance(self):
        print("Balance is {}\n".format(self.balance))
        return self.balance


class Players(Money):

    def __init__(self, name="Dealer", balance=0):
        self.name = name
        self.game = []
        self.balance = balance

    def receiveCards(self, card):
        self.game.append(card)

    def setName(self, name="Dealer"):
        new_player = input("Enter the player's name: ")
        if new_player:
            self.name = new_player
        else:
            self.name = name

    def resetGame(self):
        self.game = []

    def getName(self):
        return self.name

    def getGame(self):
        # print("show game")
        return self.game

    def getScore(self):
        return sum_cards(self.game)


class Deck():

    def __init__(self):
        # self.deck = []
        self.deck = []

    def generator(self):
        for x in ['Club-', 'Diamond-', 'Heart-', 'Spades-']:
            for y in range(1,14):
                alpha = x+str(y)
                if y in [10, 12, 13]:
                    self.deck.append((alpha, 10))
                elif y == 1:
                    self.deck.append((alpha, 1))
                    self.deck.append((alpha, 11))
                else:
                    self.deck.append((alpha, y))

    def showDeck(self):
        print(self.deck)

    def hitCard(self):
        rand_number = random.randint(0, len(self.deck)-1)
        card = self.deck[rand_number]
        return card

class Game():
    def __init__(self, bet=0):
        self.bet = bet

    def getBet(self):
        return self.bet

    def setBet(self, bet):
        self.bet = bet

def sum_cards(*args):
    sum = 0
    val = 0
    card = ""
    for x in args:
        for y in x:
            card,val = y
            sum += val
    return sum

def check_action(action=None, *args):
    if action is "H" or action is "h":
        print("\nHitting")
        game_players[player_turn].receiveCards(newdeck.hitCard())
        return sum_cards(game_players[player_turn].getGame())
    elif action is "S" or action is "s":
        print("\nStay")
        return sum_cards(game_players[player_turn].getGame())
    else:
        print("Not a valid action")


def menu(playing):
    print("")
    if playing == False:
        print("Player {}, your balance is: {}".format(game_players[player_turn].name, game_players[player_turn].balance) )
        resp = input("Do you want to continue playing (Y o N)?")
        if resp == "Y" or resp == "y":
            print("\nLet's continue playing...\n")
            return True
        else:
            exit(1)

## initialization
def initGame(*args, **kwargs):
    # two players you and the computer (dealer)

    if(reset):
        print("resetting the game")
        game_players[0].resetGame()
        game_players[1].resetGame()

    else:
        newdeck.generator()
        newdeck.showDeck()

        deposit = int(input("How much do you want to deposit? "))
        game_players[0].deposit(deposit)
        game_players[1].deposit(deposit)


    print("")
    bet_amount = int(input("How much do you want to bet? "))
    enoughBalance = game_players[0].getBalance() - bet_amount


    if enoughBalance <= 0:
        print("\nYou do not have any peny!! Get out of here\n")
        exit(1)
    else:
        game.setBet(game_players[0].withdraw(bet_amount))
        print("Game bet ", game.getBet())
        # game_players[1].bet(bet_amount)
        balance = game_players[0].getBalance()

        if balance <= 0:
            print("You do not have more money")
            print("The game is over")


        game_players[0].receiveCards(newdeck.hitCard())
        game_players[0].receiveCards(newdeck.hitCard())
        game_players[1].receiveCards(newdeck.hitCard())
        game_players[1].receiveCards(newdeck.hitCard())

        print("")
        print(game_players[1].name)
        print(game_players[1].getGame())
        print(game_players[0].name)
        print(game_players[0].getGame())

        return game, game_players, newdeck


print("\n\n\n\n\n\n\n************ Welcome to Black Jack's Simplified **************\n")
game = Game()
newdeck = Deck()
game_players = []

your_name = input("What's your name?")
player_1 = Players(name=your_name)
player_2 = Players(name="Dealer")

game_players = [player_1, player_2] #

# game initialization
playing = True # we are playing
player_turn = 0 # variable to control which player turn is

reset=False

initGame(game, game_players, newdeck, reset)

## loop throut the game
while playing:
    game_players[player_turn]
    print("")
    print("Player ", game_players[player_turn].name, ", cards: ", game_players[player_turn].getGame())

    action = input("What action do you what to take: Hit or Stay?(H or S)")

    if action == "h":
        value = check_action(action, game_players[player_turn])
        print("value ", value, " action ", action, "Player balance ", game_players[0].getBalance())

        if value > 21:
            print("Player {}, you bust!".format(game_players[player_turn].name))
            playing = False
            playing =  menu(playing)
            if playing:
                reset=True
                initGame(game, game_players, newdeck, reset)

    if action == "s":
        print("Score of the game ", game_players[player_turn].getScore())

        if player_turn == 0:
            player_turn = 1
        else:
            player_turn = 0
            playing = False
            if game_players[1].getScore() > game_players[0].getScore():
                print("Player {}, you bust!".format(game_players[0].name))
                print("Player {}, you win!".format(game_players[1].name))
                playing = menu(playing)
                if playing:
                    reset=True
                    initGame(reset)

            elif game_players[1].getScore() == game_players[0].getScore():
                print("Players are equal!! Best is to start again")
                game_players[0].deposit(game.getBet())
                print("Game bet ", game.getBet())
                playing = menu(playing)
                if playing:
                    reset=True
                    initGame(reset)

            else:
                print("Player {}, you bust!".format(game_players[1].name))
                print("Player {}, you win!".format(game_players[0].name))
                game_players[0].deposit(game.getBet())
                print("Game bet ", game.getBet())
                playing = menu(playing)
                if playing:
                    reset=True
                    initGame(reset)
