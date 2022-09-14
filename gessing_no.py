from random import randint
from art import logo

EASY_LEVEL_TURN = 10
HARD_LEVEL_TURN = 5


#function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too High")
        return turns - 1
    elif guess < answer:
        print("Too Low")
        return turns - 1
    else:
        print(f"You got it!  The answer was {answer}.")


#make function to set difficulties.
def set_difficlty():
    level = input("Chose a diffivulty. Type 'easy' or 'hard': ")
    if level == "easy":
        global turns
        return EASY_LEVEL_TURN
    else:
        return HARD_LEVEL_TURN


def game():
    print(logo)
    #choosing a random number between 1 to 100.
    print("wellcome to the no gessing game ! ")
    print("I'm thinking of a nmber between 1 and 100.")
    answer = randint(1, 100)
    # print(f"Yess, the correct answer is {answer}")

    turns = set_difficlty()

    guess = 0
    while guess != answer:
        #let the user guess a number.
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        #track the number of turns and reduces by 1 if they get it wrong
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("you've ran out at guesses, you lose.")
            break
        elif guess != answer:
            print("guess again")


#Repeat the guessing functionily if they get it worng
# print("Chaase a difficulty. Type 'easy' or 'hard': ")
game()
