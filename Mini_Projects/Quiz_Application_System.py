questions = [
    {
        "question": "Which language is used for Python programming?",
        "options": ["A. Java", "B. Python", "C. C++", "D. HTML"],
        "answer": "B"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A. function", "B. define", "C. def", "D. fun"],
        "answer": "C"
    },
    {
        "question": "Which data type stores key-value pairs?",
        "options": ["A. List", "B. Tuple", "C. Set", "D. Dictionary"],
        "answer": "D"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["A. //", "B. #", "C. /*", "D. --"],
        "answer": "B"
    },
    {
        "question": "Which function is used to get input from the user?",
        "options": ["A. scan()", "B. get()", "C. input()", "D. read()"],
        "answer": "C"
    }
]


score = 0

print("===== PYTHON QUIZ =====")

for number, question in enumerate(questions, start=1):

    print(f"\nQuestion {number}:")
    print(question["question"])

    for option in question["options"]:
        print(option)

    answer = input("Enter your answer (A/B/C/D): ").upper()

    if answer == question["answer"]:
        print("Correct! ")
        score += 1
    else:
        print(f"Wrong!  Correct answer: {question['answer']}")


print("\n===== QUIZ RESULT =====")
print(f"Your Score: {score}/{len(questions)}")

percentage = (score / len(questions)) * 100

print(f"Percentage: {percentage:.2f}%")

if percentage >= 80:
    print("Excellent! ")
elif percentage >= 50:
    print("Good job! ")
else:
    print("Keep practicing! ")