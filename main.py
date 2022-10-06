from art import logo
import random


print(logo)
print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100")
level_of_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
the_guessed_number = random.randint(1,100)
print(the_guessed_number)
number_of_attempts_easy = 10
number_of_attempts_hard = 5
is_game_over = False
user_guess = 0


def game_analogy(guessed, actual):
    if abs(actual - guessed) < 3:
        return "Too low"
    elif abs(actual - guessed) > 10:
        return "Too high"

def counter(attempts):
    attempts-=1
    return attempts
def guessing_game():
    while not is_game_over:
        user_attempts = 0



        if level_of_difficulty == 'easy':
            user_attempts = 10
            for i in range(user_attempts):

                user_guess = int(input("Make a guess: "))

                if user_guess == the_guessed_number:
                    print("Congratulations you have the right guess")
                    is_game_over = True
                    break
                else:
                    user_attempts-=1


                    if user_attempts == 0:
                        print("Game over")
                        is_game_over = True
                    else:

                        print(f"You still have {user_attempts} remaining attempts")
                        print(game_analogy(user_guess, the_guessed_number))

        elif level_of_difficulty == 'hard':
            user_attempts = 5
            for i in range(user_attempts):

                user_guess = int(input("Make a guess: "))

                if user_guess == the_guessed_number:
                    print("Congratulations you have the right guess")
                    is_game_over = True
                    break
                else:
                    user_attempts -= 1

                    if user_attempts == 0:
                        print("Game over")
                        is_game_over = True
                    else:

                        print(f"You still have {user_attempts} remaining attempts")
                        print(game_analogy(user_guess, the_guessed_number))
guessing_game()

