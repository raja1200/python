import random , time 


def getUserChoice():
    userChoice = input("Enter Your Choice(rock/paper/scissor) : ").lower()
    while userChoice not in ["rock" , "paper" , "scissor"]:
         userChoice = input("Invalid Choice ! \n Enter Your Choice(rock/paper/scissor) : ").lower()
    return userChoice

def getCompChoice():
    choices = ["rock" , "paper" , "scissor"]
    return random.choice(choices)

def determineWinner(userchoice , computerChoice):
    if (userchoice == computerChoice) :
        return "It's a Tie !"
    elif (userchoice == "rock" and computerChoice == "scissor"):
        return "You Win !"
    elif (userchoice == "paper" and computerChoice == "rock"):
        return "You Win !"
    elif (userchoice == "scissor" and computerChoice == "paper"):
        return "You Win !"
    else:
        return "Computer Wins"
    
def tryAgain():
    key1 = int(input("Enter 1 to Continue : "))
    while (key1 == 1):
        playGame()

def playGame():
    print()
    print("Welcome to Rock - Paper - Scissors !")
    userChoice = getUserChoice()
    computerChoice = getCompChoice()
    print(f"You Chose {userChoice} , and the Computer Chose {computerChoice}...")
    result = determineWinner(userChoice , computerChoice)
    time.sleep(3)
    print(result)
    print()
    tryAgain()



playGame()
