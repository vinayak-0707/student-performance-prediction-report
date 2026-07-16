# 🎓 Student Performance Predictor

A simple AI web app that predicts a student's academic performance category
based on 5 factors: attendance, study hours, previous scores, assignment
completion, and class participation.
---

## Project Information

| Field | Details |
|---|---|
| Name | [Vinayak Pandey]
| Institution | [ABES INSTITUTE OF TECHNOLOGY/Dr. A.P.J. Abdul Kalam Technical University ] |
| Submission Date | [16-07-2026] |

---

## 📌 Overview

This project is a beginner-friendly introduction to applying machine
learning in a web app. A student fills in a short form, and a trained
Decision Tree model predicts whether their performance is likely to be
**Excellent**, **Good**, **Average**, or **At-Risk** — along with a simple
tip for improvement.

## ✨ Features

- Clean, simple web form (no login required)
- AI prediction using a Decision Tree model (scikit-learn)
- Instant result with a short, actionable tip
- Fully offline / runs on your own computer
- Beginner-friendly, heavily-commented code

## 🛠️ Tech Stack

- **Python 3** — programming language
- **Flask** — web framework (serves the pages)
- **scikit-learn** — the machine learning library (trains the model)
- **pandas** — loads and organizes the dataset
- **HTML/CSS** — the web page itself

## 📁 Project Structure

```
student_performance_simple/
├── app.py                     # The Flask web app (form + prediction)
├── generate_data.py            # Creates the sample training dataset
├── train_model.py              # Trains the Decision Tree model
├── prepare_real_dataset.py     # (Optional) converts a real Kaggle dataset to our format
├── requirements.txt
├── data/
│   └── students.csv            # The training data (synthetic, or real if you use Kaggle data)
├── templates/
│   ├── index.html               # The input form page
│   └── result.html              # The prediction result page
├── static/
│   └── style.css                # Page styling
└── model.pkl                   # The trained model (created after running train_model.py)
```

## ▶️ How to Run

```bash
# 1. Install the required packages
pip install -r requirements.txt

# 2. Create the training data
python generate_data.py

# 3. Train the model
python train_model.py

# 4. Start the web app
python app.py
```

Then open the link shown in the terminal (usually **http://127.0.0.1:5000/**)
in your browser, fill in the form, and click "Predict my performance".

## 📊 Dataset

### Included: synthetic sample data
By default, `generate_data.py` creates **300 made-up student records**
using a simple formula (better attendance/study/scores → better
performance, plus some randomness). This is only for learning and testing
— it is not real student data.

### Optional: real data from Kaggle
For a more realistic project, you can train on the **Student Performance
Factors** dataset from Kaggle instead:

🔗 **https://www.kaggle.com/datasets/lainguyn123/student-performance-factors**

This is a public dataset of 6,607 real (anonymized) student records with
columns for attendance, study hours, previous scores, tutoring sessions,
motivation level, and final exam score, among others.

**To use it:**
1. Create a free Kaggle account and download the dataset CSV from the link
   above.
2. Save it as `data/StudentPerformanceFactors.csv` in this project.
3. Run:
   ```bash
   python prepare_real_dataset.py
   ```
   This converts it into the same format `train_model.py` expects
   (it maps the closest matching columns — see the comments inside
   `prepare_real_dataset.py` for exactly how).
4. Run `python train_model.py` again to retrain on the real data.

## 🧠 How the AI Model Works

The model is a **Decision Tree Classifier** — one of the easiest machine
learning models to understand. It learns a series of yes/no questions from
the training data, for example:

```
Is attendance above 70%?
├── Yes → Is previous_score above 60?
│         ├── Yes → predict "Excellent"
│         └── No  → predict "Good"
└── No  → predict "Average" or "At-Risk"
```

The real tree the model learns is picked automatically from the training
data (not written by hand) — `train_model.py` keeps it limited to 4
questions deep (`max_depth=4`) so it stays simple enough to actually
understand, rather than an unreadable maze of hundreds of rules.

- **Model accuracy:**
 printed each time you run `train_model.py` — expect
  roughly 55-65% on 4-class prediction (versus 25% for random guessing),
  which is reasonable given only 5 simple input factors