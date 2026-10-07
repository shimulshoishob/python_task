class QuizBrain:
    def __init__(self, question_list):
        self.question_list = question_list
        self.num_questions = 0
        self.score = 0

    def ask_question(self,a_question):
        print(f"Q.{self.num_questions+1}:{a_question.question_text}?(True/False)")
        self.num_questions += 1

    @staticmethod
    def solution(a_question, user_input):
        if user_input == a_question.question_answer:
            print("Correct")
            return True
        else:
            print("Incorrect")
            return False
    def score_manage(self,answer):
        if not answer != True:
            self.score += 1

