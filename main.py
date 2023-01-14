from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///workouts.db'
db = SQLAlchemy(app)


from exercises import Workout

upper1 = Workout(name="Barbell Bench Press", length="Long", exercise_type="Weightlifting", intensity="High", link="https://www.youtube.com/watch?v=rT7DgCr-3pg")
upper2 = Workout(name="Dumbbell Incline Bench Press", length="Medium", exercise_type="Weightlifting", intensity="Medium", link="https://www.youtube.com/watch?v=8iPEnn-ltC8")
upper3 = Workout(name="Dumbbell Chest Flys", length="Medium", exercise_type="Weightlifting", intensity="Medium", link="https://youtu.be/eozdVDA78K0?t=33")
upper4 = Workout(name="Dumbbell Hammer Curls", length="Medium", exercise_type="Weightlifting", intensity="Medium", link="https://youtu.be/zC3nLlEvin4?t=22")
upper5 = Workout(name="Rope Pushdowns", length="Medium", exercise_type="Weightlifting", intensity="Medium", link="https://youtu.be/vB5OHsJ3EME?t=16")
upper6 = Workout(name="Bench Tricep Dips", length="Short", exercise_type="Weightlifting", intensity="Low", link="https://youtu.be/0326dy_-CzM?t=18")
upper7 = Workout(name="Barbell Military Press", length="Long", exercise_type="Weightlifting", intensity="High", link="https://www.youtube.com/watch?v=sBt6610fUiE")
upper8 = Workout(name="Dumbbell Front Raises", length="Short", exercise_type="Weightlifting", intensity="Low", link="https://youtu.be/gzDawZwDC6Y?t=5")
upper9 = Workout(name="Machine Lateral Raises", length="Short", exercise_type="Weightlifting", intensity="Low", link="https://www.youtube.com/watch?v=0FUpcwj_1z4")
upper10 = Workout(name="Lat Pulldowns", length="Medium", exercise_type="Weightlifting", intensity="Medium", link="https://youtu.be/1VcmFW5diOU?t=5")
upper11 = Workout(name="Rope Face Pulls", length="Medium", exercise_type="Weightlifting", intensity="Medium", link="https://www.youtube.com/watch?v=eFxMixk_qPQ")
upper12 = Workout(name="Cable Back Rows", length="Medium", exercise_type="Weightlifting", intensity="Medium", link="https://youtu.be/GZbfZ033f74?t=11")

db.session.add(upper1)
db.session.add(upper2)
db.session.add(upper3)
db.session.add(upper4)
db.session.add(upper5)
db.session.add(upper6)
db.session.add(upper7)
db.session.add(upper8)
db.session.add(upper9)
db.session.add(upper10)
db.session.add(upper11)
db.session.add(upper12)

db.create_all()
db.session.commit()

@app.route('/random')
def random_exercise():
    all_exercises = Workout.query.all()
    random_exercise = random.choice(all_exercises)
    return render_template('random.html', exercise=random_exercise)

@app.route("/")
def test():
    return "<h1>Test</h1>"

if __name__ == "__main__":
    app.run(debug=True)