from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface
import html

#TODO: Create the List of Question, each question should be of the Qusetion() class
question_bank = []
for question in question_data:
    question_text = html.unescape(question["question"])
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


#TODO: Create a Quiz class, and pass it the list of questions
quiz = QuizBrain(question_bank)

#TODO: Pass the quiz class to the quiz interface
quiz_interface = QuizInterface(quiz)


# while quiz.still_has_questions():
#     quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")


# 