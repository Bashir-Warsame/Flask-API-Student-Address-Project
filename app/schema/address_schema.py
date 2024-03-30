from app.models.address import Address
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


class AddressSchema(SQLAlchemyAutoSchema):
    """Serializable schema for the Post model."""

    class Meta:
        model = Address
        fields = ("id",
                  "student",
                  "number",
                  "house_name",
                  "road",
                  "city",
                  "state",
                  "country",
                  "zipcode")

