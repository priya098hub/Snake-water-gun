import random

# Computer makes a random choice
computer = random.choice([-1, 0, 1])

# User input
you = input("Enter your choice (s for Snake, w for Water, g for Gun): ").lower()
youDict = {"s": 1, "w": -1, "g": 0}

# Validate input
if you not in youDict:
    print("Invalid choice. Please restart the game and choose s, w, or g.")
else:
    you = youDict[you]

    # Game logic
    if computer == -1 and you == 1:  # Snake drinks Water
        print("You chose Snake. Computer chose Water.")
        print("You Win!")
    elif computer == -1 and you == 0:  # Gun sinks in Water
        print("You chose Gun. Computer chose Water.")
        print("You Lose!")
    elif computer == 1 and you == -1:  # Snake drinks Water
        print("You chose Water. Computer chose Snake.")
        print("You Lose!")
    elif computer == 1 and you == 0:  # Gun kills Snake
        print("You chose Gun. Computer chose Snake.")
        print("You Win!")
    elif computer == 0 and you == -1:  # Water sinks Gun
        print("You chose Water. Computer chose Gun.")
        print("You Win!")
    elif computer == 0 and you == 1:  # Gun kills Snake
        print("You chose Snake. Computer chose Gun.")
        print("You Lose!")
    else:  # Tie condition
        print("Both chose the same. It's a Tie!")
