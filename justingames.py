#########################################
#Author: Justin Michael Cook            #
#Last Updated: 5:04PM 11th of July, 2016#
#This work is licensed under a Creative #
#Commons Attribution-ShareAlike 4.0     #
#International License                  #
#########################################


#List of games included
#Blackjack, Make a Diamond, Random Number Game
#To use please put in the "Lib" folder in your Python 3.5 folder


#Import modules
import random
import sys




#Get their name, print out games/how to access
name = input("Hello, what is your name? \n")
print('''The current games are:
Blackjack, to play write justingames.blackjack()
Make a Diamond, to play write justingames.makeadiamond()
Random Number Game, to play write justingames.rannumgame()''')




#Blackjack Game
def blackjack():
    #Greeting
    print("\nHello " +name)
    print('''The rules of this game are:
    Blackjack pays out 5:2
    Winning pays out 2:1
    Ties pay out 1:1
    Dealer will try to tie or beat you
    Player goes first \n''')


    
    #Global Variables
    global chips,playerWins,dealerWins,playerCards,playerCardsValue,dealerCards,dealerCardsValue,cardSuits,cards
    playerWins = 0
    dealerWins = 0



    #Getting initial chip amount
    chips = 0
    while True:
        try:
            chips = int(input('How many chips do you buy in with? \n'))
            break
        except ValueError:
            print("That isn't an integer!")



    #Makes game run until player decides to end game
    while True:


        print("\n\n\n")
        print("The current tally of wins and losses are:")
        print("Wins: " + str(playerWins))
        print("Losses: " + str(dealerWins) + "\n")
        print("You currently have " + str(chips) + " chips \n")

        
        ##Declaring variables, lists
        playerCards = []
        playerCardsValue = 0
        dealerCards = []
        dealerCardsValue = 0
        cardSuits = ["Hearts","Diamonds","Spades","Clubs"]
        cards = [["Ace",2,3,4,5,6,7,8,9,10,"Jack","Queen","King"],["Ace",2,3,4,5,6,7,8,9,10,"Jack","Queen","King"],["Ace",2,3,4,5,6,7,8,9,10,"Jack","Queen","King"],["Ace",2,3,4,5,6,7,8,9,10,"Jack","Queen","King"]]


        ##Functions
        
        ###Creates a new hand whenever it is called
        def assignHand():
            cardOneSuit = random.randint(0,3)
            cardOneName = cards[cardOneSuit][random.randint(0,len(cards[cardOneSuit])-1)]
            cards[cardOneSuit].remove(cardOneName)
            cardTwoSuit = random.randint(0,3)
            cardTwoName = cards[cardTwoSuit][random.randint(0,len(cards[cardTwoSuit])-1)]
            cards[cardTwoSuit].remove(cardTwoName)
            return(cardOneSuit,cardOneName,cardTwoSuit,cardTwoName)

        ###Adds a card to the hand
        def hit():
            cardSuit = random.randint(0,3)
            cardName = cards[cardSuit][random.randint(0,len(cards[cardSuit])-1)]
            cards[cardSuit].remove(cardName)
            return(cardSuit,cardName)

        ###Retrieves value of named cards for calculating hand value
        def cardValue(card):
            try:
                if int(card):
                    return card
            except ValueError:
                if card == "Jack":
                    return 10
                elif card == "Queen":
                    return 10
                elif card == "King":
                    return 10
                elif card == "Ace":
                    return 11

        ###Changes any aces in hand to a value of one
        def checkForAce(player):
            aces = 0
            for a in range(len(player)):
                if player[a] == "Ace":
                    player[a] = 1
                    aces += 1
            return aces
        
        ###Checks to see if the hand is a blackjack (ace and jack) hand
        def checkBlackJack(cards):
            if cards[1] == "Ace" and cards[3] == "Jack" or cards[1] == "Jack" and cards[3] == "Ace":
                return True
            else:
                return False

        ###Checks for losing
        def over21Function(cardsValue,cards):
            originalValue = cardsValue
            if cardsValue > 21:
                cardsValue -= 10*checkForAce(cards)
                if cardsValue > 21:
                    return True
            if originalValue != cardsValue:
                return cardsValue
            return False

        ###Shows the first card
        def showFirstCard(cards):
            print("The dealers first card is the " + str(cards[1]) + " of " + cardSuits[cards[0]] + "\n")
        
        ###Plays the dealer
        def dealerTurn():
            global chips,dealerCards,dealerCardsValue,playerWins,dealerWins
            print("\n\nThe dealer's second card is the " + str(dealerCards[3]) + " of " + cardSuits[dealerCards[2]] + "\n")
            while True:
                ####Check for losing and aces being changed
                over21 = over21Function(dealerCardsValue,dealerCards)
                if over21 == True:
                    playerWins += 1
                    chips += 2*gameBet
                    print("The dealer went over 21! You win!")
                    if playAgain():
                        return True
                elif type(over21) == int:
                    dealerCardsValue = over21
                print("Dealer's card value is: " + str(dealerCardsValue) + "\n")
                ####Check for tie
                if dealerCardsValue == playerCardsValue:
                    print("The dealer tied you!")
                    chips += gameBet
                    if playAgain():
                        return True
                ####Check for winning
                if dealerCardsValue > playerCardsValue:
                    dealerWins += 1
                    print("The dealer beat you with a card value of " + str(dealerCardsValue))
                    if playAgain():
                        return True

                ####Takes a card if neither won nor lost
                else:
                    dealerCards += hit()
                    print("The dealer got a " + str(dealerCards[len(dealerCards)-1]) + " of " + cardSuits[dealerCards[len(dealerCards)-2]])
                    dealerCardsValue += cardValue(dealerCards[len(dealerCards)-1])

        ###Asks if the player would like to play again
        def playAgain():
            while True:
                playAgain = input("\n\nWould you like to play again? ").lower()
                if playAgain == "yes":
                    return True
                elif playAgain == "no":
                    print("The final tally of wins and losses are:")
                    print("Wins: " + str(playerWins))
                    print("Losses: " + str(dealerWins))
                    print("You leave with " + str(chips) + " chips")
                    sys.exit()
                else:
                    print("That isn't a yes or no!")
            playAgain = True


        ##Main Game

        ###Checks if player is out of chips
        if chips == 0:
            print('You ran out of chips! If you want to continue please call the game again.')
            break
        
        ###Getting bet
        while True:
            try:
                gameBet = int(input('What is your bet? \n'))
                chips -= gameBet
                break
            except ValueError:
                print("That isn't an integer!")
        
        ###Creating Hands
        playerCards = list(assignHand())
        playerCardsValue = cardValue(playerCards[1]) + cardValue(playerCards[3])
        dealerCards = list(assignHand())
        dealerCardsValue = cardValue(dealerCards[1]) + cardValue(dealerCards[3])

        ###Check for Blackjack
        if checkBlackJack(dealerCards):
            dealerWins += 1
            print("Dealer got blackjack! You lose! Their cards were " + str(dealerCards[1])+ " of " + cardSuits[dealerCards[0]] + " and " + str(dealerCards[3])+ " of " + cardSuits[dealerCards[2]])
            if playAgain():
                continue
        if checkBlackJack(playerCards):
            playerWins += 1
            chips += 2.5*gameBet
            print("You got blackjack! You win! Your cards were " + str(playerCards[1])+ " of " + cardSuits[playerCards[0]] + " and " + str(playerCards[3])+ " of " + cardSuits[playerCards[2]])
            if playAgain():
                continue

        ###Shows dealer's first card
        showFirstCard(dealerCards)

        ###Allows the player to go
        while True:

            ####Tells player their cards
            print("Your cards are:")
            for a in range(0,len(playerCards),2):
                print(str(playerCards[a+1]) + " of " + cardSuits[playerCards[a]])
            print("")
            
            ####Checks if player lost
            over21 = over21Function(playerCardsValue,playerCards)
            if over21 == True:
                dealerWins += 1
                print("You went over 21! You lose!")
                if playAgain():
                    break
            elif type(over21) == int:
                playerCardsValue = over21
            print("Your hand is currently " + str(playerCardsValue) + " points \n")
            playerAction = input("What would you like to do? ").lower()
            print("")

            ####Gives player additional card if writes hit and adds that value to their hand
            ####Lets dealer go to decide outcome of game if player passes
            if playerAction == "hit":
                playerCards += hit()
                playerCardsValue += cardValue(playerCards[len(playerCards)-1])
            elif playerAction == "pass":
                if dealerTurn():
                    break
            else:
                print("Please only enter hit or pass")




#Make a Diamond Game
def makeadiamond():
    #Greeting
    print("Hello " +name)



    #Function to make diamond
    def makeDiamond(height):

        
        ##Writes out top of diamond and defines variables needed for drawing
        print(" "*(height//2) + "*")
        loop1 = 1
        loop2 = 0
        loop3 = height - 3


        ##Loops through the given height to make top half of diamond
        for a in range(height, 1, -2):
            print(" "*(a//2-1) + "*" + " "*loop1 + " "*loop2 + "*")
            loop1 += 1
            loop2 += 1


        ##Loops through the given height to make botton half of diamond
        for a in range(1,height//2,1):
            print(" "*a  + "*" + " "*loop3 + "*")
            loop3 -= 2


        ##Prints out bottom of diamond
        print(" "*(height//2) + "*")



    #Runs game
    while True:


        ##Grabs user input and runs diamond function, after asks to play again
        try:
            diamondSize = int(input("How large would you like the diamond? "))
            print(diamondSize)
            if diamondSize % 2 == 0:
                makeDiamond(diamondSize)
            else:
                print("Your diamond is an odd number! Reducing the size by one!")
                makeDiamond(diamondSize-1)

            ###Loop to playagain, yes restarts main loop and no exits program
            while True:
                playAgain = input("Do you want to play again? ").lower()
                if playAgain == "yes":
                    break
                elif playAgain == "no":
                    sys.exit()
                else:
                    print("That isn't a yes or no answer!")


        ##Restarts main loop if user doesn't enter a number
        except TypeError:
            print("That isn't a number!")
        except NameError:
            print("That isn't a number!")




#Random Number Game
def rannumgame():
    #Game loop
    while True:


        ##Generates random number, resets guesses, greets user
        try:
            therange = int(input('Hello ' + name +' What would you like the maximum number to be? \n'))
        except NameError:
            print("That isn't a number!")
        except ValueError:
            print("That isn't a number!")
        secretNumber = random.randint(1,therange)
        guesses = 0
        print('What is your guess, between 1 and ' + str(therange) + '?')


        ##Main game loop
        while True:

            ###Gets users guess and adds one to total guesses
            try:
                guess = int(input())
                guesses += 1

            ###Restarts loop if guess is not a number
            except ValueError:
                print("That isn't a integer!")

            ###Compares guess to generated number, ends game if correct
            try:
                if guess == secretNumber:
                    print('Congrats! You guessed correctly! It took you ' + str(guesses) + ' tries!')
                    break
                elif guess >= secretNumber:
                    print('Your guess is too high! Guess again!')
                else:
                    print('Your guess is too low! Guess again!')

            ###Not sure why I have this, I think it helps to ensure program doesn't break
            except ValueError:
                print("That isn't a integer!")


        ##Asks player if they would like to play again and then ends program or restarts game
        print('Would you like to play again?')
        playAgain = input().lower()
        while True:
            if playAgain == 'yes':
                break
            elif playAgain == 'no':
                sys.exit()
            else:
                print("Please enter yes or no")
