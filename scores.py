import json, random

def get_scores():

    try:
        with open("scores.json", "r") as file:
            scores = json.load(file)
            # print(scores)
            # print()
            
            print("***TOP SCORES***")
            print()
            for item in scores:
                print(f"{item["player"]}      {item["correct answers"]}     {item["score"]:.0f}")

            # return scores

    except FileNotFoundError:
        print("File not Found")
        return []

def save_scores(player, correct_answers, score, path="scores.json"):
    # print("SAVE CALLED", player, correct_answers, score)
    try:
        with open(path, "r") as f:
            data_set = json.load(f)

    except FileNotFoundError:
        print("File not found - enter a request to create")
        data_set = [] 

    except json.JSONDecodeError:
        print("History file is empty or invalid")
        data_set = []

    entry = {
        "player": player,
        "correct answers": correct_answers,
        "score": score
        }

    data_set.append(entry)
    data_set.sort(key=lambda item: item["score"], reverse=True)
    data_set = data_set[-10:]
    # print("SAVE OUTPUT", entry)

    with open("scores.json", "w") as f:
        json.dump(data_set, f, indent=2)


# get_scores()
# data = ["JWS", "20", "150"]
# save_scores(data[0],data[1],data[2])


