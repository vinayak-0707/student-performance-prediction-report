import pickle

from flask import Flask, render_template, request

app = Flask(__name__)

# Load the model we trained earlier (once, when the app starts)
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Simple tips shown depending on the prediction - a beginner-friendly
# stand-in for a more advanced recommendation system.
TIPS = {
    "Excellent": "Great work! Keep up your current study habits.",
    "Good": "You're doing well. A little more study time could push you into 'Excellent'.",
    "Average": "Try attending more classes and studying a bit more consistently.",
    "At-Risk": "Your predicted performance is low. Try to improve attendance and study hours, and consider talking to a teacher.",
}


@app.route("/")
def home():
    # Just show the empty form
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    # Step 1: read the 5 numbers the student typed into the form
    attendance = float(request.form["attendance"])
    study_hours = float(request.form["study_hours"])
    previous_score = float(request.form["previous_score"])
    assignment_completion = float(request.form["assignment_completion"])
    participation = float(request.form["participation"])

    # Step 2: ask the trained model to make a prediction.
    # scikit-learn expects a 2D list, even for just one student.
    features = [[attendance, study_hours, previous_score, assignment_completion, participation]]
    prediction = model.predict(features)[0]
    tip = TIPS.get(prediction, "")

    # Step 3: show the result page
    return render_template("result.html", prediction=prediction, tip=tip)


if __name__ == "__main__":
    app.run(debug=True)
