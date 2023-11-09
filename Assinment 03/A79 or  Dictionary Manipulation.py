student_scores = {
    "Alice": 90,
    "Bob": 85,
    "Charlie": 78,
    "David": 92
}

student_name = input("Enter the student's name: ")
student_score = int(input("Enter the student's score: "))

if student_name in student_scores:

    student_scores[student_name] = student_score
    print(f"Updated {student_name}'s score to {student_score}")
else:

    student_scores[student_name] = student_score
    print(f"Added {student_name} with a score of {student_score}")

print("Updated Student Scores:")
for name, score in student_scores.items():
    print(f"{name}: {score}")
