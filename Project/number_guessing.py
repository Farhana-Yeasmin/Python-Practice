import random
import math

lower = int(input("Enter lower bound:"))
upper = int(input("Enter upper bound:"))

# Generating random number between lower bound to upper bound

x = random.randint(lower,upper)

guessing_number = round(math.log(upper-lower+1,2))

print("\n\tYou've only", guessing_number,"chances to guess the integer!\n")

# Initializing the number of guesses.
count=0

while count < guessing_number:
    #  we cancelling the count people to zero initially
    count+=1

    # taking guessing number as input
    guess = int(input("Guess a number:"))

    if x ==guess:
        print("Congratulations you did it in",count,"try")
        break
    elif x> guess: 
        print('You guessed too small!!')
    elif x< guess:
        print("You guessed to high!")     

    # If guessing is more than required guesses then show this output
    if count>= guessing_number:
        print("\nThe number is %d"%x)
        print('\tBetter Luck Next Time!')
