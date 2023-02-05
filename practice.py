from dict import dictionary
import random


def focused_practice():
    global focused_guess_list, focused_guess_choice, focused_guess, guess_count
    if practice_list_count == 0:
        guess_count = 0
    else:
        focused_guess_list = random.choice(practice_list)
        focused_guess_choice = focused_guess_list["chinese"]
        focused_guess = input(f" Focused guess the character: {focused_guess_choice} \n")
        check_answer_focused()


def check_answer_focused():
    global practice_list_count
    if focused_guess in focused_guess_list.values():
        print("Correct.")
        practice_list_count -= 1
    else:
        print("Incorrect")
        practice_list_count += 1


def check_answer():
    global guess, guess_list, guess_choice, practice_list, guess_count
    if guess in guess_list.values():
        print("Correct.")
    else:
        print("Incorrect")
        practice_list.append(guess_list)
        guess_count += 1

guess_count = 0
practice_list_count = 5
practice_list = []

while True:
    print(f" This is the guess count: {guess_count}")
    print(f" This is the practice count: {practice_list_count}")
    if guess_count < 4 or practice_list_count == 0:
        practice_list_count = 5
        guess_list = random.choice(dictionary)
        guess_choice = guess_list["chinese"]
        guess = input(f"Guess the character: {guess_choice} \n")
        check_answer()
    else:
        focused_practice()

