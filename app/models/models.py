from sqlmodel import SQLModel, Field
from datetime import date
import enum from
from typing import Optional

class DriverLicenseApplication(SQLModel, table=True):
    __tablename__ = "license_applications"

    id: int = Field(primary_key=True)
    last_name: str = Field(nullable=False)
    first_name: str = Field(nullable=False)
    middle_name: str = Field(default=None)
    license_number: str = Field(unique=True, nullable=False)
    date_of_birth: date = Field(nullable=False)
    sex: SexEnum = Field(nullable=False)
    height_cm: int = Field(nullable=False)
    residential_address: str = Field(nullable=False)
    mailing_address: str = Field(default=None)
    province: str = Field(nullable=False)
    postal_code: str = Field(nullable=False)

print("models.py loaded")


'''
Steps to creating models:
1. Import SQLModel and Field from sqlmodel
2. Create class NameofModel(SQLModel, table=True)
    - table=True is used to create a table in the database
    - __tablename__ is used to name the table in the database
3. Add fields to the model
  

Notes
Models are for
- defining the structure of the table in the database
- defining constraints
- It is EVERYTHING DATABASE

The database model doesn't care about frontend-specific rules or user input validation.

Fields:
  - Fields are created using Field() from sqlmodel
  - Fields are used to define the structure of the table in the database
  - Define constraints

'''