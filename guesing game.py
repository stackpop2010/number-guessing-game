import random

def guessing_game(guess, guessme=None):

    if guessme == None:
        guessme = random.randint(1,10)

    if guess == guessme:
        print("you win! the secret number is ", guessme)
    
    if guess > 10 or guess < 1:
        guess = int(input("invalid input, please guess a number between 1 and 10 "))
        return(guessing_game(guess, guessme))
    if guess > guessme:
        guess = int(input("guess too high, try again "))
        return (guessing_game(guess, guessme))
    if guess < guessme:
        guess = int(input("guess too low, try again "))
        return (guessing_game(guess, guessme))


my_guess=int(input("guess a number between 1 and 10 "))
guessing_game(my_guess)