from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for data in question_data:
    question_bank.append(Question(data["question"], data["correct_answer"]))

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz_brain.score}/{len(question_bank)}")
