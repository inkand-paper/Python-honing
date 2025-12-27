import random

def guess_game():
    
    secret_number = random.randint(1, 50)
    attempts = 0
    guessed_correctly = False

    print("I'm thinking of a number between 1 and 50.")

    
    while not guessed_correctly:
        user_input = input("Enter your guess: ")
        
        
        if not user_input.isdigit():
            print("Please enter a whole number.")
            continue
            
        guess = int(user_input)
        attempts += 1 

        
        if guess == secret_number:
            print(f" Correct! It took you {attempts} attempts.")
            guessed_correctly = True
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print("Too low! Try again.")


guess_game()
