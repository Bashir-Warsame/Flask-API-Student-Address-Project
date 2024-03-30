from app.database import db


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    nationality = db.Column(db.String(100))
    city = db.Column(db.String(100))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    gender = db.Column(db.String(10))
    age = db.Column(db.Integer)
    english_grade = db.Column(db.String(10))
    math_grade = db.Column(db.String(10))
    sciences_grade = db.Column(db.String(10))
    language_grade = db.Column(db.String(10))

    address = db.relationship('Address', back_populates='student')
