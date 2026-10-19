import random, copy, time  # normal python modules
import quiz, scores # seperate line for python programs with define functions

def play_game():
    start_time = time.time()
    # print(quiz.questions)
    questions = copy.deepcopy(quiz.get_questions())
    # print(questions)
    
    count = 1
    Easy_Correct = 0
    Medium_Correct = 0
    Hard_Correct = 0
    
    for nextup in questions:
    #     print(json.dumps(item, indent=2))
    
        random.shuffle(nextup["options"])
                
        answer_index = nextup["options"].index(nextup["answer"])
        letters = ["A","B","C","D"]
        correct_answer = letters[answer_index]
                
                
        print(f"Question {count}: {nextup["question"]}")
        print(f"A: {nextup["options"][0]}")
        print(f"B: {nextup["options"][1]}")
        print(f"C: {nextup["options"][2]}")
        print(f"D: {nextup["options"][3]}")
    
        guess = input("Your guess?\n").upper()

        while guess.upper() not in letters:
            guess = input("You did not enter a valid option try again: ")
    
        if guess == correct_answer: 
            if nextup["difficulty"] == "Easy":
                Easy_Correct += 1
            elif nextup["difficulty"] == "Medium":
                 Medium_Correct += 1
            else: 
                 Hard_Correct += 1
                
        count += 1
        Total_Correct = Easy_Correct + Medium_Correct + Hard_Correct
        Score = (Total_Correct / 20)*100
    
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    
    if elapsed_time < 60:
        speed_bonus = 20
    elif elapsed_time < 90:
        speed_bonus = 10
    elif elapsed_time < 120:
        speed_bonus = 5
    else:
        speed_bonus = 0

    Score = Score + speed_bonus 
    
    print(f"Thank You for Playing - you got {Total_Correct} right including {Hard_Correct} hard, {Medium_Correct} medium and {Easy_Correct} easy for a score of {Score:.0f}!")
    return Total_Correct, Score

while True:

    choice = input("Would you like to play a game? If yes, enter Y - otherwise S for high scores and Q to quit:  ")

    while choice.upper() not in ["Y","Q","S"]:
        choice = input("You did not enter a valid option try again: ")


    if choice.upper() == "Y":
        name = input("Please enter your 3 initials:  ").upper()
        while len(name) != 3:
            name = input("3 letters please:  ").upper()
        correct_answer, score = play_game()
        scores.save_scores(name, correct_answer, score)
           

    elif choice.upper() == "Q":
        break

    elif choice.upper() == "S":
        scores.get_scores()

    else:
        break
    
