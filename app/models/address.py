from app.database import db


class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    number = db.Column(db.String(50))
    house_name = db.Column(db.String(100))
    road = db.Column(db.String(100))
    city = db.Column(db.String(100))
    state = db.Column(db.String(100))
    country = db.Column(db.String(100))
    zipcode = db.Column(db.String(20))

    student = db.relationship('Student', back_populates='address')
