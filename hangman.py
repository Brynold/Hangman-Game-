""" Hi, lets play Hangman """
from Hangman.guss_data import Guess_Data

""" Welcome to my channel..!"""
import random


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def introduction():
    print(bcolors.HEADER + "Welcome to Hangman game ..!\n")
    name = input("Enter your name please : \n")
    print(f"Hello ,{name}")
    print(f"Best of luck {name}")
    print("This game is above to start..\n")
    print("-------------------------------")


""" lets create global variable"""


def variables():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    # data_list = Guess_Data.get_data()
    word = random.choice(Guess_Data.get_data())
    length = len(word)
    count = 0
    display = '_' * length
    already_guessed = []
    play_game = ""


""" lets create function for tear down the execution """


def termination():
    global play_game
    play_game = input(bcolors.ENDC + "Do you want to play again ?\nif y= YES and n=NO")
    """ check for correct input data """
    while play_game.lower() not in ["n", "y"]:
        play_game = input(bcolors.ENDC + "Do you want to play again ?\nif y= YES and n=NO")

    if play_game == "y":
        variables()
    elif play_game == "n":
        print(bcolors.OKCYAN + "Thanks for playing. C U later .. ")
        exit()


"""lets add some colour to the console """


def play_hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit = 5
    print(bcolors.OKGREEN + f"This is hangman words : {display}")
    guess = input(bcolors.OKGREEN + "Enter your guesses :")
    """ strip is used for remove edge spaces in the input string .."""
    guess = guess.strip()
    if len(guess) == 0 or len(guess) >= 2 or guess <= "9":
        print(bcolors.FAIL + "Invalid Input , Try again later ..")

    elif guess in word:
        already_guessed.extend([guess])
        index_count = word.find(guess)
        """ we used slicing for guess string """
        word = word[:index_count] + "_" + word[index_count + 1:]
        display = display[:index_count] + guess + display[index_count + 1:]
        print(display + "\n")
    else:
        count += 1
        """ or  count = count+1 """
        if count == 1:
            print(bcolors.OKCYAN+"   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print(bcolors.WARNING + f"Wrong answer : {str(limit - count)}: Guesses remaining")

        elif count == 2:
            print(bcolors.OKCYAN+"   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print(bcolors.WARNING + f"Wrong answer : {str(limit - count)}: Guesses remaining")

        elif count == 3:
            print(bcolors.OKCYAN+"   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")

            print(bcolors.WARNING + f"Wrong answer : {str(limit - count)}: Guesses remaining")

        elif count == 4:

            print(bcolors.OKCYAN+"   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print(bcolors.WARNING + f"Wrong answer : {str(limit - count)}: Guesses remaining")

        elif count == 5:
            print(bcolors.OKCYAN+"   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print(bcolors.FAIL + f"Wrong answer. Your Hangman  ")
            print(bcolors.FAIL + f"The word you missed to guess is {word}")
            termination()

    if word == '_' * length:
        print(bcolors.OKGREEN + "Congrats , You have Guessed the word correctly...!")
        termination()

    elif count != limit:
        play_hangman()


introduction()
variables()
play_hangman()
