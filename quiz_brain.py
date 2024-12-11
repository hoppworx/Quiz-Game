# QuizBrain
    ## attributes:
        ## question_number = 0
        ## questions_list
    ## method:
        ## next_question()

# TODO-1: Ask question
    ## Example:  Q.1: A slug's blood is green. (True/False)?:

# TODO-2: Check if answer was correct
# TODO-3: Check if we're at the end of the quiz

class QuizBrain:
    def __init__(self,q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = (input(f"Q.{self.question_number}: {current_question.text} (True/False): "))
        self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self):
        # if len(self.question_number) < len(self.question_list):
        #     return True
        # else:
        #     return False
        # Below replaces code above (since it also simply returns True if condition is True
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer,correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")

