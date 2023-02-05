from dict import dictionary
import random
from tkinter import *

root = Tk()
root.geometry('600x600')


pract_dict = []
practice_value = 10

def question_list():
    global q_list, pract_dict, dictionary
    print(len(pract_dict))
    if len(pract_dict) < 6:
        q_list = dictionary
        print("This is from regular list")
    else:
        q_list = pract_dict
        print("you have entered focused list")
        practice_value += 5


def get_q():
    global q_set, q_list, q
    q_set = random.choice(q_list)
    q = q_set["chinese"]

def practice_count_down(): 
    global practice_value   
    if practice_value < 1:
        pract_dict.clear()
        question_list()
    else:
        get_q()

def test_answer():
    global answer, practice_value
    if answer in q_set.values():
        print("Yes")
        if practice_value > 0:
            practice_value -= 1
            practice_count_down()
    else:
        print("No")
        practice_value += 1
        pract_dict.append(q_set)


while True:
    
    question_list()
    get_q()
    print(f"Practice count: {pract_dict} and practice value {practice_value}")
    guess_label = Label(root, text=q, font=("Helvetica", 75), bg="white", fg="black")
    guess_label.grid(row=0, column=0, padx=10)
    
    

    answer = input(f"What is it? {q}")
    test_answer()

pract_label = Label(root, text=practice_value, font=("Helvetica", 75), bg="white", fg="red")
pract_label.grid(row=0, column=1, padx=10)


root.mainloop()











# #randomly select a dictionary from list
# x = random.choice(dictionary)
# #randomly selected dictionary from list
# print(x['english'], x['chinese'], x['pinyin'], x['enYin'])
# #Chooses chinese key to print 'chinese' value
# print(x['chinese'])
# #X is a 'dict'
# print(type(x))
# print(*x.items(), sep='\n')
# random_x = random.choice(list(x.items()))
# print(type(random_x))
# print(random_x)
# print(random_x[1])

