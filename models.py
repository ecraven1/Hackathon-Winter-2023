from datetime import datetime
from fitvidapphackathon import db

class User(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(20), unique=True, nullable=False)
        email = db.Column(db.String(120), unique=True, nullable=False)
        image_file = db.Column(db.String(20), nullable=False, default='jpeg')
        password = db.Column(db.String(60), nullable=False)
        new_exercises = db.relationship('NewExercise', backref='instructor', lazy=True)

        def  __repr__(self):
            return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class NewExercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    exercise_name = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def  __repr__(self):
        return f"NewExercise('{self.exercise_name}', '{self.date_posted}')"