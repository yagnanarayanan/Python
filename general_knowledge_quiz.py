# Provide users with 5 questions with 4 options to each question. Get user option as input and compare it with the
# answer key and print out the score at the end showing the correct answers as well.
questions = ('Which planet is known as the "Red Planet"?',
             "Which country is famous for producing maple syrup?",
             "What is the chemical symbol for gold?",
             'Who painted the famous artwork "Mona Lisa"?',
             'What is the largest organ in the human body?'
             )
options = (("a) Earth", "b) Mars", "c) Jupiter", "d) Venus"),
           ("a) Spain", "b) Canada", "c) Japan", "d) Australia"),
           ("a) Go", "b) Ag", "c) Au", "d) Gd"),
           ("a) Michelangelo", "b) Vincent van Gogh", "c) Leonardo da Vinci", "d) Pablo Picasso"),
           ("a) Liver", "b) Brain", "c) Heart", "d) Skin"))
answers = ('b', 'b', 'c', 'c', 'd')
guesses = []
question_counter = 0
score = 0
for question in questions:
    print(question)
    for option in options[question_counter]:
        print(option)
    question_counter += 1
    guess = input("Enter your answer option as a,b,c or d: ")
    guesses.append(guess.lower())
print(f"Your guesses: {guesses}")
print(f"Correct answers: {answers}")
answer_counter = 0
while answer_counter < len(questions):
    if guesses[answer_counter] == answers[answer_counter]:
        score += 1
    answer_counter += 1
print(f"Your score: {score}")
