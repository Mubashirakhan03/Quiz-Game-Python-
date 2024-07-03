class QuizBrain:
    def __init__(self,q_list):
        self.question_number=0
        self.question_list=q_list
        self.score=0
    def still_has_questions(self):
        return self.question_number<len(self.question_list)

    def next_question(self):
        current_question=self.question_list[self.question_number]
        self.question_number+=1
        user_answere=input(f"Q{self.question_number}: {current_question.text} (True/False): ")
        self.check_answere(user_answere, current_question.answere)
    def check_answere(self, user_answere, correct_answere):
            if user_answere.lower() == correct_answere.lower():
                self.score+=1
                print("You got it right!")
            else:
                print("You got it wrong")

            print(f"The correct answere was {correct_answere}.")
            print(f"your score is {self.score}/{self.question_number}")
            print("\n")