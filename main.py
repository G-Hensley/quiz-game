from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

# Create a list of Question objects
question_bank = []
for q_dict in question_data:
    question_bank.append(Question(q_dict["question"], q_dict["correct_answer"]))

# Initialize the QuizBrain with the list of Question objects
quiz = QuizBrain(question_bank)

# Continue the quiz until all questions are answered
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")
