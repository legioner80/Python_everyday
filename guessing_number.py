# Guess number game
import random

print("Hello! What is your name?")
name = input()

print(name + " I am thinking of a number between 1 and 20 ")
secretNumber = random.randint(1, 20)

for guessesTaken in range(1, 6):
    print('Take a guess.')
    guess = int(input())
    if guess < secretNumber:
        print("Your guess is too low.")
    elif guess > secretNumber:
        print("Your guess is too high.")
    else:
        break  # This condition is for the correct guess!
if guess == secretNumber:
    print('Excellent, ' + name + '! You guessed my number in ' + str(guessesTaken) + ' guesses.')
else:
    print('NO.The number I was thinking of was ' + str(secretNumber))

print('DEBUG: Secret number is ' + str(secretNumber))
