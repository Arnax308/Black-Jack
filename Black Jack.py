import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    
    def __str__(self):
        return f'{self.rank} of {self.suit}'
    
class Deck:
    
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                #Using Card class to make all the cards
                self.deck.append(Card(suit,rank)) 
    
    def __str__(self):
        
        #Creating an empty string 
        deck_comp = ''
        
        for i in self.deck:
            
            #Basically a for loop to append name of cards in a single variable
            #I would have prefred a list but you cannot concatenate a list with other strings
            #Also looks like __str__ doesnt support lists
            
            deck_comp += '\n '+ i.__str__() 
        
        return 'The deck has:' + deck_comp

    def shuffle(self):
        
        #Using random library to shuffle the deck
        random.shuffle(self.deck)
        
    def deal(self):
        
        #Returning the popped card because this popped card will be put on table or will be used to play
        return self.deck.pop()
    

class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        
        #Appending card to our player from Deck()
        #card will be replaced by the Deck.deal() in the actual game
        self.cards.append(card)
        
        #Since its a card, from the above fuctions, it has a value
        #Therefore getting the value of the card too
        self.value += values[card.rank]
        
        #Tracking aces
        if self.value == 'Ace':
            self.aces += 1
    
    def adjust_for_ace(self):
        
        #When the total value > 21 and the player has an ace
        #We are using self.aces as an boolean value
        #Python takes 0 as False and the rest of the numbers as True 
        #So the below loop is same as 
        #while self.vale > 21 and self.aces > 0
        #This will run only and only if you have a ace
        #If you dont have any ace then self.aces will be 0, which is basically false and hence the loop will not run!
        
        while self.value > 21 and self.aces: 
            
            self.value -= 10
            self.aces -= 1

class Chips:
    
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        #If the player wins, there total will be increased by the bet
        self.total += self.bet 
    
    def lose_bet(self):
        #Similarly if the player loses, there total will be subtracted by the bet
        self.total -= self.bet

def take_bet(chips):
    
    bet = True
    while bet:
        
        try:
            Chips.bet = int(input('Please input your bet: ')) 
            
        except:
            print('The bet must be a number!!\nTry again') 
            
        else: 
            if chips.bet > chips.total:
                print(f'You dont have enough funds.\nTake a value less than or equal to{chips.total}')
                
            else:
                bet = False

def hit(deck,hand):
    
    #Adding the dealing card from Deck() to the Hand() that is the player
    hand.add_card(deck.deal())
    #Then adjusting for aces likewise
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    
    while True:
        x = input("Would you like to Hit or Stand? Enter 'h' or 's' ")
        
        if x[0].lower() == 'h':
            hit(deck,hand)  # hit() function defined above

        elif x[0].lower() == 's':
            print("Player stands. Dealer is playing.")
            playing = False

        else:
            print("Sorry, please try again.")
            continue
        break

def show_some(player,dealer):
    
    #Showing Dealer's card
    print("\nThe Dealer's hand is : ")
    print("<Card is hidden!!>")
    
    #Showing second card as one card is always hidden, which is generally the 1st card
    print(dealer.cards[1])
    
    #Showing Player's hand/card
    # 2 of them
    
    print("\nThe Player's hand is : ", *player.cards, sep = '\n')
    
    #Where * is used instead of the for loop, this works same as the for loop
    #Every item is printed
    #To put every item in new line sep = '\n' is used
    #This same has been done in complete solution, due to which u were confused 
    
def show_all(player,dealer):
    
    #Showing all Dealer's Cards
    print('\n')
    print("The Dealer's hand is : ",*dealer.cards, sep='\n ')

    #Showing and Calculating Value of Dealer's Card
    print(f"The value of Dealer's card is {dealer.value}")
    
    #Showing all Player's cards
    print("\nThe Player's hand is : ",*player.cards, sep='\n ')

    #Showing and Calculating Value of Player's Card
    print(f"The value of Player's card is {player.value}")
    
def player_busts(player,dealer,chips):
    print('The player is busted ＞︿＜')
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print('The player wins!!! ヾ(^▽^*)))')
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print('The dealer is busted!!! ヾ(^▽^*)))')
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print('The dealer wins!!! ＞︿＜')
    chips.lose_bet()
    
def push(player,dealer):
    print("Dealer and Player scores the same points!! It's a push!")

while True:
    # Print an opening statement
    print('Welcome to BlackJack! Get as close to 21 as you can without going over!\n\
    Dealer hits until she reaches 17. Aces count as 1 or 11.')
    
    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()
    
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
            
    # Set up the Player's chips
    player_chips = Chips()  # remember the default value is 100    
    
    # Prompt the Player for their bet
    take_bet(player_chips)
    
    # Show cards (but keep one dealer card hidden)
    show_some(player_hand,dealer_hand)
    
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck,player_hand) 
        
        # Show cards (but keep one dealer card hidden)
        show_some(player_hand,dealer_hand)  
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break        


    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17 
    if player_hand.value <= 21:
        
        while dealer_hand.value < 17:
            hit(deck,dealer_hand)    
    
        # Show all cards
        show_all(player_hand,dealer_hand)
        
        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)

        else:
            push(player_hand,dealer_hand)        
    
    # Inform Player of their chips total 
    print("\nPlayer's winnings stand at",player_chips.total)
    
    # Ask to play again
    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")
    
    if new_game[0].lower()=='y':
        playing=True
        continue
    else:
        print("Thanks for playing!")
        break