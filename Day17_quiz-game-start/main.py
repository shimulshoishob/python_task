from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

quiz_question = [] # make object list

for i in range(len(question_data)):
    quiz_question.append(Question(question_data[i]["text"], question_data[i]["answer"]))

quiz = QuizBrain(quiz_question)
j=0
while j < len(quiz_question):
    a_question = quiz.question_list[j]
    quiz.ask_question(a_question)
    user_input = str(input("Answer: "))
    user_input = user_input.title()
    answer = quiz.solution(a_question, user_input)
    quiz.score_manage(answer)
    print(f"Score:{quiz.score}/{quiz.num_questions}")
    j+=1