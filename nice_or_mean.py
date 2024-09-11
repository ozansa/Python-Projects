# nice_or_mean.py

def start(nice=0, mean=0, name=""):
    # Get the user's name
    name = describe_game(name)
    nice, mean, name = nice_mean(nice, mean, name)

def describe_game(name):
    """
    Describe the game and check if it's a new or returning player.
    """
    # Check if the player's name is empty
    if name != "":
        # Returning player
        print("\nThank you for playing again, {}!".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = input("\nWhat is your name? \n>>> ").capitalize()
                if name != "":
                    print("\nWelcome, {}!".format(name))
                    print("\nIn this game, you will be greeted by several people.")
                    print("You can choose to be nice or mean, but your fate will be sealed by your actions.")
                    stop = False
    return name

def nice_mean(nice, mean, name):
    """
    This function defines the game logic where the user can choose to be nice or mean.
    """
    stop = True
    while stop:
        show_score(nice, mean, name)
        pick = input("\nA stranger approaches you for a conversation. Will you be nice or mean? (N/M) \n>>>: ").lower()
        if pick == "n":
            print("\nThe stranger walks away smiling...")
            nice += 1
            stop = False
        elif pick == "m":
            print("\nThe stranger glares at you menacingly and storms off...")
            mean += 1
            stop = False
        else:
            print("\nPlease enter 'N' for nice or 'M' for mean.")
        
        score(nice, mean, name)  # Check the score after each choice

def show_score(nice, mean, name):
    """
    This function displays the current score.
    """
    print("\n{}, your current total: ({} Nice, {} Mean)".format(name, nice, mean))

def score(nice, mean, name):
    """
    This function checks the score and determines if the player wins or loses.
    """
    if nice > 2:
        win(nice, mean, name)
    elif mean > 2:
        lose(nice, mean, name)
    else:
        nice_mean(nice, mean, name)

def win(nice, mean, name):
    """
    Player wins if they have been nice more than twice.
    """
    print("\nNice job {}, you win! Everyone loves you and you've made lots of friends along the way!".format(name))
    again(nice, mean, name)

def lose(nice, mean, name):
    """
    Player loses if they have been mean more than twice.
    """
    print("\nAhhhh too bad, game over! {}, you live in a dirty beat-up van by the river, wretched and alone!".format(name))
    again(nice, mean, name)

def again(nice, mean, name):
    """
    Asks the player if they want to play again.
    """
    stop = True
    while stop:
        choice = input("\nDo you want to play again? (y/n): \n>>> ").lower()
        if choice == "y":
            stop = False
            reset(nice, mean, name)
        elif choice == "n":
            print("\nOh, so sad, sorry to see you go!")
            stop = False
            quit()
        else:
            print("\nPlease enter 'Y' for 'YES' or 'N' for 'NO': \n>>>")

def reset(nice, mean, name):
    """
    Resets the game variables but keeps the player's name.
    """
    nice = 0
    mean = 0
    start(nice, mean, name)

# If the script is run directly, start the game
if __name__ == "__main__":
    start()
