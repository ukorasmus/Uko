import random
mastid = ["Hearts", "Diamonds", "Clubs", "Spades"]
numbers = ["Six of ", "Seven of ", "Eight of ", "Nine of ", "Ten of ", "Jack of ", "Queen of ", "King of ", "Ace of "]                                   
vaartused = {6 : "Six", 7 : "Seven", 8 : "Eight", 9 : "Nine", 10 : "Ten", 11 : "Jack", 12 : "Queen", 13 : "King", 14 : "Ace"}
vaartused2 = {"Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 11, "Queen": 12, "King": 13, "Ace": 14}
def durak():
    trump = ""
    deck = ["Six of Hearts", "Seven of Hearts", "Eight of Hearts", "Nine of Hearts", "Ten of Hearts", "Jack of Hearts", "Queen of Hearts", "King of Hearts", "Ace of Hearts", \
            "Six of Diamonds", "Seven of Diamonds", "Eight of Diamonds", "Nine of Diamonds", "Ten of Diamonds", "Jack of Diamonds", "Queen of Diamonds", "King of Diamonds", "Ace of Diamonds",\
            "Six of Clubs", "Seven of Clubs", "Eight of Clubs", "Nine of Clubs", "Ten of Clubs", "Jack of Clubs", "Queen of Clubs", "King of Clubs", "Ace of Clubs",\
            "Six of Spades", "Seven of Spades", "Eight of Spades", "Nine of Spades", "Ten of Spades", "Jack of Spades", "Queen of Spades", "King of Spades", "Ace of Spades"]
    playerCards = takeCards(deck)
    opponentCards = takeCards(deck)
    trump = mastid[random.randint(0, 3)]
    print("Trump: %s" % (trump))
    print("")
    print("Your cards are:")
    print("")
    for card in playerCards:
        print(card)
    print("")
    print("Opponent's cards are:")
    print("")
    for card in opponentCards:
        print(card)
    print("")
    startingPlayer(trump, opponentCards, playerCards)
def smallestTrump(trump, cards):
    for card in cards:
        smallestTrump = 0
        card = card.split(" ")
        print(card[2])
        if card[2] == trump:
            card = card.pop
            print(card)
            trumpNum = vaartused2[" ".join(card)+" "]
            print(trumpNum)
            if trumpNum < smallestTrump or smallestTrump == 0:
                smallestTrump = trumpNum
    return smallestTrump

def startingPlayer(playerCards, trump, opponentCards):
    opponentTrump = smallestTrump(trump, opponentCards)
    playerTrump = smallestTrump(trump, playerCards)
    if opponentTrump < playerTrump:
        opponentAttack(opponentCards)
    else:
        playerAttack(playerCards)

def takeCards(deck):
    playerCards = []
    opponentCards = []
    choice = "123456"
    for item in range(6):
        mast = mastid[random.randint(0, 3)] 
        num = numbers[random.randint(0, 8)]
        card = num + mast
        while not card in deck:
            mast = mastid[random.randint(0, 3)] 
            num = numbers[random.randint(0, 8)]
            card = num + mast
        startOut = random.choice(choice)
        if startOut == "1" or "2" or "3":
            playerCards.append(card)
        else:
            opponentCards.append(card)
        choice = choice.replace(startOut, "")
        deck.remove(card)
    return playerCards

def playerAttack(playerCards):
    i = 1
    print("Your cards are:")
    for card in playerCards:
        print("%s - %s" % (i, card))
        i += 1
    valik = int(input("Kaart: "))
    while not valik in range(1, i):
        k = 1
        print("Please pick a card")
        for card in playerCards:
            print("%s - %s" % (k, card))
            k += 1
        valik = int(input("Kaart: "))
        
    currentCard = playerCards[valik-1]
    print("You chose %s" % (currentCard))
    k = 0 
    for item in range(6):
        if currentCard[0] in playerCards[k][0]:
            print("You can also play %s" % (playerCards[k]))
            input("Do you want to play it? Y/N ")
            
def opponentAttack(opponentCards):
    i = 1
    print("Your cards are:")
    for card in opponentCards:
        print("%s - %s" % (i, card))
        i += 1
    valik = int(input("Kaart: "))
    while not valik in range(1, i):
        k = 1
        print("Please pick a card")
        for card in opponentCards:
            print("%s - %s" % (k, card))
            k += 1
        valik = int(input("Kaart: "))
        
    currentCard = opponentCards[valik-1]
    print("You chose %s" % (currentCard))

    
    
    
    


        
        
