# This class deals with the computation part of the quiz

class QuizBrain:

    def __init__(self, question_bank):
        '''
        Create a QuizBrain object by passing in a list of question objects.
        '''
        self.question_number = 0
        self.question_bank = question_bank
        self.score = 0

    def still_has_questions(self):
        '''
        Checks if there are more questions left in the question bank. Returns True if there are more questions
        left and False if there are none
        '''
        return self.question_number < len(self.question_bank)

    def input(self):
        '''
        Accepts an input from the user, and performs validation.
        '''
        answer = input(
            f"\nQ. {self.question_number + 1} {self.question_bank[self.question_number].text} (True/False)?: ").strip().lower()
        self.check_answer(
            answer, self.question_bank[self.question_number].answer)
        self.question_number += 1

    def check_answer(self, user_answer, correct_answer):
        '''
        Accepts the user's answer and the correct answer as inputs and returns True if the two answers are the same
        and False if not.
        '''
        if user_answer == correct_answer.lower():
            print("That was correct!")
            self.score += 1
        else:
            print(
                f"That was incorrect!\nThe correct answer was: {correct_answer}")
        print(f"Your score is {self.score}/{self.question_number + 1}")
