import random

def game_result(user_choice, computer_choice):
    # Game rules:
    # Snake vs Water -> Snake drinks water (Snake wins)
    # Water vs Gun -> Gun sinks in water (Water wins)
    # Gun vs Snake -> Gun kills Snake (Gun wins)
    
    if user_choice == computer_choice:
        return "It's a Tie!"
    elif (user_choice == "Snake" and computer_choice == "Water") or \
         (user_choice == "Water" and computer_choice == "Gun") or \
         (user_choice == "Gun" and computer_choice == "Snake"):
        return "You Win!"
    else:
        return "You Lose!"

# Choices for the game
choices = ["Snake", "Water", "Gun"]

print("Welcome to Snake, Water, Gun Game!")
print("Enter your choice: Snake, Water, or Gun")

while True:
    user_choice = input("Your choice: ").capitalize()
    if user_choice not in choices:
        print("Invalid choice, please choose again.")
        continue

    computer_choice = random.choice(choices)
    print(f"Computer's choice: {computer_choice}")
    
    result = game_result(user_choice, computer_choice)
    print(result)
    
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing! Goodbye!")
        break
