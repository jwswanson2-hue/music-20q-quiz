# creating a quiz game with questions in json and score keeping modules
import json, random


def get_questions():

    try:
        with open("quiz.json", "r") as file:
            questions = json.load(file)
            random.shuffle(questions)
            return questions
            # print(questions)

    except FileNotFoundError:
        print("File not Found")
        return []

# print(get_questions())


      