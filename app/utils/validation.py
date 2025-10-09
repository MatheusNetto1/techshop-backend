# app/utils/validation.py
def validate_not_empty(value: str, field_name: str):
    if not value or value.strip() == "":
        raise ValueError(f"{field_name} cannot be empty")
    return value