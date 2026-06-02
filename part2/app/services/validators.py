"""
Validation service layer.
Keeps business rules separate from API.
"""


class ValidationError(Exception):
    pass


def validate_email(email):
    if "@" not in email or "." not in email:
        raise ValidationError("Invalid email format")


def validate_password(password):
    if len(password) < 6:
        raise ValidationError("Password too short")


def validate_price(price):
    if price <= 0:
        raise ValidationError("Price must be greater than 0")


def validate_latitude(lat):
    if lat < -90 or lat > 90:
        raise ValidationError("Invalid latitude")


def validate_longitude(lon):
    if lon < -180 or lon > 180:
        raise ValidationError("Invalid longitude")


def validate_rating(rating):
    if rating < 1 or rating > 5:
        raise ValidationError("Rating must be 1–5")