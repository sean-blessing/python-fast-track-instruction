# Pseudocode
# 1. Define a dictionary to store scores: student_scores
student_scores = {}

# 2. Read the testscores.dat file into student_scores dictionary
#    - key: student_name, value: num_test_score
with open("./scripts/files/testscores.dat") as scores_in:
    for line in scores_in:
        student_name, num_test_score = line.rstrip("\n\r").split(":")
        num_test_score = int(num_test_score)
        # store in dictionary
        student_scores[student_name] = num_test_score    
    
# 3. Print, one per line, the student_name, num_test_score, and letter_grade
print("Student Grade Summary:")
print("=================================")
for student_name, num_test_score in student_scores.items():
    # - will have to convert the num_test_score to a letter_grade
    grade = 'F'
    if num_test_score > 94:
        grade = 'A'
    elif num_test_score > 88:
        grade = 'B'
    elif num_test_score > 82:
        grade = 'C'
    elif num_test_score > 74:
        grade = 'D'
    
    # :20s adds padding
    print(f'{student_name:20s} {num_test_score} {grade}')

# 4. After printing individual scores, print the average score
sum_of_scores = sum(student_scores.values())
average = sum_of_scores / len(student_scores)
print(f'Average Score = {average}')
