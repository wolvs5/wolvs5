#Write a game where the computer draws a random integer between 1 and 10.
# The user tries to guess the number until they guess the right number.
# After each guess the program prints out a text: Too high, Too low or Correct.
# Notice that the computer must not change the number between guesses.

import random
number=random.randint(1,10)
guess = int(input("Guess a number between 1 and 10: "))
while guess != number:
     if guess > number:
         print("Too high")
     elif guess < number:
         print("Too low")

     guess = int(input("Guess a number between 1 and 10: "))
print("Congrats! You guessed the number in " + str(number) + "!")
