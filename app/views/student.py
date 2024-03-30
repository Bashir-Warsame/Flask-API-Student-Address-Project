from flask import Blueprint, request, jsonify
from app.database import db
from app.models.student import Student

student_bp = Blueprint('student', __name__)


# Endpoint to create a new student
@student_bp.route('/api/student', methods=['POST'])
def create_student():
    data = request.get_json()
    new_student = Student(
        id=data['id'],
        name=data['name'],
        nationality=data['nationality'],
        city=data['city'],
        latitude=data['latitude'],
        longitude=data['longitude'],
        gender=data['gender'],
        age=data['age'],
        english_grade=data['english_grade'],
        math_grade=data['math_grade'],
        sciences_grade=data['sciences_grade'],
        language_grade=data['language_grade']
    )
    db.session.add(new_student)
    db.session.commit()
    return jsonify({'message': 'Student created successfully'}), 201


# Endpoint to get all students
@student_bp.route('/api/student', methods=['GET'])
def get_students():
    students = Student.query.all()
    result = []
    for student in students:
        result.append({
            'id': student.id,
            'name': student.name,
            'nationality': student.nationality,
            'city': student.city,
            'latitude': student.latitude,
            'longitude': student.longitude,
            'gender': student.gender,
            'age': student.age,
            'english_grade': student.english_grade,
            'math_grade': student.math_grade,
            'sciences_grade': student.sciences_grade,
            'language_grade': student.language_grade

        })
    return jsonify(result)


# Endpoint to get a student by ID
@student_bp.route('/api/student/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = Student.query.get(student_id)
    if student:
        return jsonify({
            'id': student.id,
            'name': student.name,
            'nationality': student.nationality,
            'city': student.city,
            'latitude': student.latitude,
            'longitude': student.longitude,
            'gender': student.gender,
            'age': student.age,
            'english_grade': student.english_grade,
            'math_grade': student.math_grade,
            'sciences_grade': student.sciences_grade,
            'language_grade': student.language_grade
        })
    else:
        return jsonify({'message': 'Student not found'}), 404


# Endpoint to update a student's details
@student_bp.route('/api/student/<int:student_id>', methods=['PATCH'])
def update_student(student_id):
    student = Student.query.get(student_id)
    if not student:
        return jsonify({'message': 'Student not found'}), 404

    data = request.get_json()
    if 'name' in data:
        student.name = data['name']
    if 'nationality' in data:
        student.nationality = data['nationality']
    if 'city' in data:
        student.city = data['city']
    if 'latitude' in data:
        student.latitude = data['latitude']
    if 'longitude' in data:
        student.longitude = data['longitude']
    if 'gender' in data:
        student.gender = data['gender']
    if 'age' in data:
        student.age = data['age']
    if 'english_grade' in data:
        student.english_grade = data['english_grade']
    if 'math_grade' in data:
        student.math_grade = data['math_grade']
    if 'sciences_grade' in data:
        student.sciences_grade = data['sciences_grade']
    if 'language_grade' in data:
        student.language_grade = data['language_grade']

        db.session.commit()
        return jsonify({'message': 'Student updated successfully'})


# Endpoint to delete a student
@student_bp.route('/api/student/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    student = Student.query.get(student_id)
    if not student:
        return jsonify({'message': 'Student not found'}), 404

    db.session.delete(student)
    db.session.commit()
    return jsonify({'message': 'Student deleted successfully'})
