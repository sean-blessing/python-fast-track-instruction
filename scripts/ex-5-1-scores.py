# Read testscores.dat into dictionary
# - key: student name, value: numeric test score
# Print out student names, numeric score and letter grade
# Print avg score

def convert_score_grade(score):
    grade = ""
    if score >= 95:
        grade = "A"
    elif score >= 89:
        grade = "B"
    elif score >= 83:
        grade = "C"
    elif score >=75:
        grade = "D"
    else:
        grade = "F"
    return grade

print("Welcome to the test scores app!\n")

scores_dict = {}

with open("./scripts/files/testscores.dat") as scores_in:
    for line in scores_in:
        name, score = line.rstrip('\n\r').split(":")
        scores_dict[name] = int(score)

score_total = 0
print(f"Student                 Score   Grade")

for name, score in sorted(scores_dict.items()):
    score_total += score
    grade = convert_score_grade(score)
    print(f"{name:20s}\t{score}\t{grade}")

avg_score = score_total / len(scores_dict)
print(f"\n==== Avg Score: {avg_score}")

print("Bye")