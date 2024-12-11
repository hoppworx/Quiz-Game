from types import NoneType

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


# Create question_bank to contain a list of question objects, each being initialized with a question and an answer
## Write a for loop to iterate over the question_data.  Create a Question object from each entry in question_data.
## Append each Question object to the question_bank.


question_bank = []

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(q_text=question_text, q_answer=question_answer)
    question_bank.append(new_question)

# print(question_bank[0].text)
# print(question_bank[0].answer)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    guess = quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}. {int(quiz.score/quiz.question_number * 100)}%")



