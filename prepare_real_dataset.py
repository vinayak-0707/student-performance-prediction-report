import os
import pandas as pd

RAW_PATH = "data/StudentPerformanceFactors.csv"
OUTPUT_PATH = "data/students.csv"

MOTIVATION_TO_PARTICIPATION = {"Low": 3, "Medium": 6, "High": 9}


def main():
    if not os.path.exists(RAW_PATH):
        print(f"Could not find {RAW_PATH}.")
        print("Download it from https://www.kaggle.com/datasets/lainguyn123/student-performance-factors")
        print(f"and save it as {RAW_PATH}, then run this script again.")
        return

    df = pd.read_csv(RAW_PATH)

    # Drop rows with missing values in the columns we actually use
    needed_columns = ["Attendance", "Hours_Studied", "Previous_Scores",
                       "Tutoring_Sessions", "Motivation_Level", "Exam_Score"]
    df = df.dropna(subset=needed_columns)

    # Scale Tutoring_Sessions (a small integer, e.g. 0-8) up to a 0-100 "completion" style number
    max_sessions = df["Tutoring_Sessions"].max()
    assignment_completion = (df["Tutoring_Sessions"] / max_sessions * 100).round(1)

    participation = df["Motivation_Level"].map(MOTIVATION_TO_PARTICIPATION).fillna(5)

    # Bucket the real Exam_Score into 4 categories using quantiles, so the
    # classes stay reasonably balanced regardless of this dataset's actual
    # score distribution.
    q15, q50, q85 = df["Exam_Score"].quantile([0.15, 0.50, 0.85])

    def bucket(score):
        if score >= q85:
            return "Excellent"
        elif score >= q50:
            return "Good"
        elif score >= q15:
            return "Average"
        else:
            return "At-Risk"

    out = pd.DataFrame({
        "attendance": df["Attendance"],
        "study_hours": df["Hours_Studied"],
        "previous_score": df["Previous_Scores"],
        "assignment_completion": assignment_completion,
        "participation": participation,
        "performance": df["Exam_Score"].apply(bucket),
    })

    out.to_csv(OUTPUT_PATH, index=False)
    print(f"Converted {len(out)} real student records -> {OUTPUT_PATH}")
    print(out["performance"].value_counts())
    print("\nNow run: python train_model.py")


if __name__ == "__main__":
    main()
