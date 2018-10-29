#import the random package so that we can generate random numbers
from random import randint
#from colorama import Fore, Back, Style

#choices is an array => a container that can hold multiple items
#arrays are 0-based -> the first item is 0, the second is 1, etc
choices = ["rock", "paper", "scissors"]
player = False

#make the computer choose a weapon from the choices array at random
computer_choice = choices[randint(0,2)]

#print the choices to the terminal window
print("computer chooses: ", computer_choice)

#set lives
playerLives = 3
computerLives = 3
#print(playerLives,computerLives)
print()
print("You have", playerLives, "lives left")
print("Computer has", computerLives, " lives left")
print()


# set up our loop
while player is False:
    print("You have", playerLives, "lives left")
    print("Computer has", computerLives, " lives left")
    
    # set palyer to true by making a selection
    print("Choose your weapon!")
    player = input("Rock, Paper or scissors? \n")

    print()

#to quit n restart    
    print("Do you wanna quit or restart?")
# to quit
    if player == "quit":
       exit()
# to restart

    if player == "restart":
       playerLives = 3
       computerLives = 3
       player = False
       computer_choice = choices[randint(0,2)]

    print()

#chooses player n computer
    print("Your choice:", player)
    print("Computer's choice:", computer_choice, "\n")

# check for a tie = choices ar thge same
    if (computer_choice == player):
        print("it's a tie, you live to shoot another day")
    
#for ROCK
# check to see if the computer choices beats our choice or not
    elif player == "rock":
        if computer_choice == "paper":
           playerLives = playerLives - 1
# computer won
           print("you lose! paper covers rock")
        else:
         computerLives = computerLives - 1
# we win
         print("you won", player, "smashes", computer_choice)

#for PAPER
    elif player == "paper":
        if computer_choice == "scissors":
           playerLives = playerLives - 1 

# computer won
           print("you lose!", computer_choice, "cut", player)
        else:

# we win
           computerLives = computerLives - 1
           print("you won", player, "covers", computer_choice)

#For SCISSORS
    elif player == "scissors":
        if computer_choice == "Rock":
            playerLives = playerLives - 1 

# computer won
            print("you lose!", computer_choice, "smashes",  player)
        else:

# we win
            computerLives = computerLives - 1
            print("you win", player, "cut", computer_choice)
    
    else:
        print("Check your spelling... that's not a valid choice\n")


# reset the game loop and start over again
    player = False
    computer_choice = choices[randint(0,2)]
#set to restart or to quit when game over (player loses)    
    while playerLives == 0:
      print()
      print("You have", playerLives, "lives left")
      print("Computer has", computerLives, " lives left")
      print("Amazing :D , You're the best <3")
      player = input("restart or quit ??\n")
      if player == "restart":
         playerLives = 3
         computerLives = 3
         player = False
         computer_choice = choices[randint(0,2)]
      if player == "quit":
         exit()
      else:
         print("Check your spelling ...")

#set to restart or to quit when game over (computer loses)  
    while computerLives == 0:
      print()
      print("You have", playerLives, "lives left")
      print("Computer has", computerLives, " lives left")
      print("Amazing :D , You're the best <3")
      player = input("restart or quit ??\n")
      if player == "restart":
         playerLives = 3
         computerLives = 3
         player = False
         computer_choice = choices[randint(0,2)]
      if player == "quit":
         exit()
      else:
         print("Check your spelling ...")