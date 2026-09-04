score_input = input("Enter a score (0-100): ")
score = int(score_input)

if score < 0 or score > 100:
    print("Error: Invalid score. Please enter a value between 0 and 100.")
else:
    if score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 60:
        grade = "C"
    elif score >= 50:
        grade = "D"
    else:
        grade = "F"
    
    print(f"A score of {score} earns grade: {grade}")
