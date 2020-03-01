import random
import re


def main():
    intro()
    word_bank = {1: "dog", 2: "cat", 3: "home", 4: "friend", 5: "tight", 6: "ozmo", 7: "car", 8: "photo",
                 9: "town", 10: "drink", 11: "burger", 12: "burrito", 13: "cow", 14: "taco"}
    word = word_bank[random.randint(1, len(word_bank))]
    word_split = []
    answer = []
    used = []
    duplicate_answer = False
    solved = False
    for i in word:
        word_split.append(i)
        answer.append(" _")
    tries = 6
    print("")
    while tries != 0 and solved is not True:
        print_board(answer)
        letter = user_input()

        duplicate_answer = check_guesses(letter, used)
        if duplicate_answer is True:
            print("You already used the letter %s." % letter)
        else:
            if letter not in word_split:
                print("There is no %s in the word." % letter)
                tries -= 1
                print("Tries left: %s" % tries)
            else:
                for i in range(len(word_split)):
                    if letter == word_split[i]:
                        answer[i] = letter
                    else:
                        pass
        used.append(letter)
        solved = check_if_solved(answer)
        print("")

    if tries == 0:
        print("You lose! The word was %s." % word)
    elif tries > 0:
        print("Congrats, you won! The word was: %s" % word)
    print("Thanks for playing!")


def check_guesses(letter, used):
    for i in range(len(used)):
        if letter in used[i]:
            return True
    return False


def check_if_solved(answer):
    blanks = 0
    for i in range(len(answer)):
        if answer[i] == " _":
            blanks += 1
    if blanks == 0:
        return True
    else:
        return False


def intro():
    print("Welcome to Hangman! Simply guess the letters in the word within 6 tries to win.")


def print_board(answer):
    for i in range(len(answer)):
        print(" " + answer[i], end="")
    print("")


def user_input():
    string_check = re.compile('[a-z]')
    while True:
        letter = input("> ").lower().strip()
        if len(letter) > 1 or len(letter) < 1:
            print("Please input a single letter.")
        elif string_check.search(letter) is None:
            print("Please input a letter.")
        else:
            break
    return letter


main()
