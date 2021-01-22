# Author: Ty Vareka
# Date: 1/21/2020
# Description: Number guessing game that tells you if your guess is too high or too low
Guesses = 1
print("Enter the number for the player to guess.")
answer = int(input())
print("Enter your guess.")
num_guess = int(input())
while num_guess != answer:
    Guesses += 1
    if num_guess > answer:
        print("Too high - try again:")
        num_guess = int(input())
    elif num_guess < answer:
        print("Too low - try again:")
        num_guess = int(input())
print("You guessed it in", Guesses, "tries.")
