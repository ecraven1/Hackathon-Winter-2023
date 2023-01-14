from main import db
#from flask_sqlalchemy import SQLAlchemy

#db = SQLAlchemy()

class Workout(db.Model):
    _id = db.Column("id",db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    length = db.Column(db.String(10))
    exercise_type = db.Columnn(db.String(20))
    intensity = db.Column(db.String(20))
    link = db.Column(db.String(200))

    def __init__(self, name, length, exercise_type, intensity, link):
        self.name = name
        self.length = length
        self.exercise_type = exercise_type
        self.intensity = intensity
        self.link = link