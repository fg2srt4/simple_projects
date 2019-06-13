import random

# step 1, generate the random number
def answer():
    answer = random.randint(0, 100)
    return answer


# step 2, get user's name
def intro():
    print("Hello, welcome to the number guessing game.")
    print("What is your name? ")
    name = str(input('Name: '))
    return name


# function to get user's number guess and ensure it is an integer
def guess():

    guess = input("Guess: ")
    
    try:
        val = int(guess)
        return val

    except ValueError:
        print("You can only enter numbers in this program.")
        print("Rebooting...\n")
        main()
        

# main function, checks users guess agains the answer, asks again if wrong
def main():
    name = intro()
    answer1 = answer()
    print("Alright %s, I am thinking of a number, between 0 and 100" % name)
    print("What number am I thinking of?")
    guess1 = guess()

    while guess1 != answer1:
        if guess1 > 100 or guess1 < 0:
            print("Sorry, I said between 0 and 100")
            guess1 = guess()
            
        elif guess1 > answer1:
            print("Sorry, you've guessed too high")
            guess1 = guess()

        elif guess1 < answer1:
            print("Sorry, you've guessed too low")
            guess1 = guess()

    print("Exactly! You guessed the right number")


main()
            
        
