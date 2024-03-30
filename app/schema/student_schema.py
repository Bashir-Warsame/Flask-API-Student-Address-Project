from app.serializer import ma
from app.models.student import Student
from app.schema.address_schema import AddressSchema
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


class StudentSchema(SQLAlchemyAutoSchema):
    """Serializable schema for the User SQLAlchemy object."""

    class Meta:
        # Provide the User model to serialize.
        model = Student

        # Define the fields which will be in the output when User model is serialized.
        fields = ("id",
                  "name",
                  "nationality",
                  "city",
                  "latitude",
                  "longitude",
                  "gender",
                  "age",
                  "english_grade",
                  "math_grade",
                  "sciences_grade",
                  "language_grade")

    addresses = ma.Nested(AddressSchema, many=True)
