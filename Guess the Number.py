# This is a guess the number game.
import random

# ask the user for their name
print('What is your name? ')
name = input()

# greet the user and generate the random number
print('Well, ' + name + ", I'm thinking of a number from 1 to 20.")
secretNumber = random.randint(1, 20)

guess = None  # start the variable 'guess' with no value

# for loop, so that it can break after the designated range/number of guesses
for guessesTaken in range(1, 7):
    print('Take a guess.')

    # fix the error if the user doesn't input a number
    try:
        guess = int(input())
    except ValueError:
        print("Invalid input. This is a number guessing game. Please input a number.")
        continue  # continue the code after catching the error.

    if guess < secretNumber:
        print("Your guess is too low.")
    elif guess > secretNumber:
        print("Your guess is too high.")
    else:
        break

# resolve the game.
if guess == secretNumber:
    print('Good job ' + name + '! You guessed my number in ' + str(guessesTaken) + ' guesses.')
else:
    print('Out of guesses. The number was ' + str(secretNumber) + ".")

