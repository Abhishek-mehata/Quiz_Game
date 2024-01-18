print("********************")
print("Welcome to my Quiz Game!!!")

# question_bank = [
#         {"text":"The ability of one class to acquire methods and attributes of another class is called ___.","answer":"A"},

#         {"text":"Which of the following is a type of inheritance?","answer":"D"}    ,

#         {"text":"What type of inheritance has multiple subclasses to a single superclass?","answer":"C"},

#         {"text":"What is the depth of multilevel inheritance in python?","answer":"C"},

#         {"text":"What does MRO stands for?","answer":"D"}
#     ]

# # answers = ["A", "D", "C", "C", "B"]

# options = [["A. Inheritance", "B. Abstraction", "C. Polymorphism", "D. Objects"],
#            ["A. Single", "B. Double", "C. Multiple", "D. both A and C"],
#            ["A. Multiple Inheritance", "B. MultiLevel Inheritance", "C. Hierarchical inheritance", "D. None of these"],
#            ["A. Two level", "B. Three level", "C. Any level", "D. None of these"],
#            ["A. Method Recursive Object", "B. Method Resolution Order", "C. Main Resolution Order",
#             "D. Method Resolution Object"]
#            ]
import game_database 
import os
score = 0
def check_answer(user_guess,correct_ans):
    if user_guess==correct_ans:
        # return False
        return True
    else:
        return False
for question_num in range(len(game_database.question_bank)):
    print("****************************************")
    print(game_database.question_bank[question_num]['text'])
    for i in game_database.options[question_num]:
        print(i)
    # user_guess
    guess=input("Enter your answer(A/B/C/D): ").upper()
    is_correct=check_answer(guess,game_database.question_bank[question_num]['answer'])
    if is_correct:
        # PendingDeprecationWarning
        print("COrrect answer")
        score=score+1
        print(f"Your score is {score}/{question_num+1}")
    else:
        print("Incorrect")
        print(f"the correct answer is: {game_database.question_bank[question_num]['answer']}")
        print(f"Your score is {score}/{question_num+1}")
os.system("CLS")
print("****************************************")
print(f"You have gave {score} correct Answers.")
print(f"Your score is {(score/len(game_database.question_bank))*100}%")

