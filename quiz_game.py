print("===== PYTHON QUIZ GAME =====")

score = 0

questions = [
    {
        "question": "Which language are we learning?",
        "options": ["A. Java", "B. Python", "C. C++", "D. HTML"],
        "answer": "B"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["A. //", "B. <!-- -->", "C. #", "D. **"],
        "answer": "C"
    },
    {
        "question": "Which function is used to display output?",
        "options": ["A. input()", "B. print()", "C. display()", "D. show()"],
        "answer": "B"
    },
    {
        "question": "Which data type stores True or False?",
        "options": ["A. String", "B. Integer", "C. Boolean", "D. Float"],
        "answer": "C"
    }
]

for q in questions:
    print("\n" + q["question"])

    for option in q["options"]:
        print(option)

    answer = input("Enter your answer: ").upper()

    if answer == q["answer"]:
        print("Correct! ✅")
        score += 1
    else:
        print("Wrong! ❌")

print("\n===== RESULT =====")
print("Your Score:", score, "/", len(questions))

if score == len(questions):
    print("Excellent! 🏆")
elif score >= 2:
    print("Good job! 👍")
else:
    print("Keep practicing! 💪")