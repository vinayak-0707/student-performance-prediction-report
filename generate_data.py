import csv
import random

random.seed(42)  # makes the "random" numbers the same every time we run this

NUM_STUDENTS = 300


def make_one_student():
    attendance = random.randint(30, 100)        # percent
    study_hours = random.randint(0, 30)          # hours per week
    previous_score = random.randint(0, 100)      # percent
    assignment_completion = random.randint(0, 100)  # percent
    participation = random.randint(1, 10)        # class participation rating

    # A simple made-up formula for how "good" the student's total score is.
    # Each factor is scaled to a 0-100 range first, then weighted, so the
    # final total naturally lands somewhere between 0 and 100.
    total = (
        attendance * 0.25
        + (study_hours / 30 * 100) * 0.20
        + previous_score * 0.25
        + assignment_completion * 0.15
        + (participation / 10 * 100) * 0.15
    )
    total = total + random.randint(-12, 12)  # add some randomness, like real life
    total = max(0, min(100, total))          # keep it between 0 and 100

    # Turn the number into a simple category
    if total >= 72:
        label = "Excellent"
    elif total >= 55:
        label = "Good"
    elif total >= 38:
        label = "Average"
    else:
        label = "At-Risk"

    return [attendance, study_hours, previous_score, assignment_completion, participation, label]


def main():
    rows = [make_one_student() for _ in range(NUM_STUDENTS)]

    header = [
        "attendance", "study_hours", "previous_score",
        "assignment_completion", "participation", "performance",
    ]

    with open("data/students.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)

    print(f"Created data/students.csv with {NUM_STUDENTS} student records.")


if __name__ == "__main__":
    main()
