from dict import dictionary
import random


class QuizBrain:

    def __init__(self):
        pass

    



    def next_question(self):
        random_characters = random.choice(dictionary)
        print(random_characters)
