def run_quiz(questions):
    score = 0
    for question, options, answer in questions:
        print(question)
        for idx, option in enumerate(options, 1):
            print(f"{idx}. {option}")
        user_answer = int(input("Enter your answer (1-4): "))
        if user_answer == answer:
            print("Correct!")
            score += 1
        else:
            print("Wrong!")
    print(f"You got {score} out of {len(questions)} questions correct.")

# Sample questions data
questions = [
    ("What is the capital of France?", ["London", "Paris", "Berlin", "Rome"], 2),
    ("What is the largest mammal?", ["Elephant", "Whale", "Giraffe", "Horse"], 2),
    ("Which planet is known as the Red Planet?", ["Mars", "Venus", "Jupiter", "Mercury"], 1)
]

# Run the quiz
run_quiz(questions)
