from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

# for element in question_data:
#     for q,a in element.items():
#         new_question = Question(q,a)
#         question_bank.append(new_question)

for q in question_data:
    question_text = q["text"]
    question_answ = q["answer"]
    new_question = Question(question_text,question_answ)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)


while quiz.still_has_questions():

    quiz.next_question()



print("You completed the quiz!")
print(f"Your final scores was: {quiz.score}/{quiz.question_number}")

    