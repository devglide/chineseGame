from dict import dictionary
from quiz_brain_china import QuizBrain
from question_model import Question
import random


def evaluate_guess():
    global temp_value_list, focused_practice
    if x in temp_value_list:
        print("you got it")
        temp_value_list = []
        
    else:
        print("sorry, better luck next time")
        practice_list.append(random_characters)
        #print(f"This has been added to your practice list: {random_characters}")
        temp_value_list = []
        focused_practice += 1
        print(focused_practice)

def evaluate_focused_guess():
    global temp_value_list, escape_practice_hell
    if x in temp_value_list:
        print("you got it")
        temp_value_list = []
        escape_practice_hell -= 1
        print(escape_practice_hell)
    else:
       print("sorry, better luck next time") 


#print a greeting
print("Welcome to the Chinese guessing game!")
#start game
play_game = True
practice_list = []
temp_value_list = []
focused_practice = 0
escape_practice_hell = 10

while play_game:
    #print(practice_list)
    if len(practice_list) >= 5:
        play_game = False
        

    random_characters = random.choice(dictionary)
    for i in random_characters.values():
        temp_value_list.append(i)
    #print(temp_value_list)
    #print(random_characters)
    guess = random_characters['chinese']
    guess_eng = random_characters['english']
    #print(guess)
    x = input(f"What does this character mean {guess}")
    evaluate_guess()

while not play_game:
    print(f"You are in focused game. Number of correct attemps before you can escape hell: {escape_practice_hell}")
    focused_guess = random.choice(practice_list)
    for i in focused_guess.values():
        temp_value_list.append(i)
    focused_guess = temp_value_list['chinese']
    guess_eng = temp_value_list['english']
    #print(guess)
    x = input(f"What does this character mean {focused_guess}")
    evaluate_focused_guess()
    



