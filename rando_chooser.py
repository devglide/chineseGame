from dict import dictionary
import random


wrong_answer_count = 0
wrong_answer_list = []
escape = 10




def check_answer():
    global rando_dict, rando_dict, guess, wrong_answer_count
    if guess in rando_dict.values():
        print('You are correct')
    else:
        print('You are incorrect')
        wrong_answer_count += 1
        wrong_answer_list.append(rando_dict)

def check_answer_wrong():
    global rando_dict_wrong, rando_prompt_wrong, guess, escape_wrong, wrong_answer_count
    if guess in rando_dict.values():
        print('You are correct')
        escape -=.5
    else:
        print('You are incorrect')
       




while main_game True:
    wrong_answer_count <= 5:
    rando_dict = random.choice(dictionary)
    rando_prompt = (rando_dict['chinese'])

    print(f'Guess {rando_prompt}')
    guess = input()
    check_answer()t%    
    # print(wrong_answer_count)
    # print(wrong_answer_list)

while main_game False:
    print(wrong_answer_count)
    rando_dict_wrong = random.choice(wrong_answer_list)
    rando_prompt_wrong = (rando_dict_wrong['chinese'])

    print(f'Guess {rando_prompt_wrong}')
    guess = input()
    check_answer_wrong()
        














# print(*rando_dict.items(), sep='\n')
# all_pairs = list(rando_dict.items())
# print(30*'-')
# print(all_pairs[2])
#-----------------------------------------
#rando_tuple = list(rando_dict.items())