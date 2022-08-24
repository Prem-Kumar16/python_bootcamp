from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for qn in question_data:
    q_text = qn["text"]
    q_answer = qn["answer"]
    q1 = Question(q_text, q_answer)
    question_bank.append(q1)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You've completed the Quiz")
print(f"Your final score is {quiz.score}/{quiz.question_number}")
