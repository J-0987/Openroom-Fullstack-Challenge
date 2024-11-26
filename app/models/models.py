ffrom typing import Optional
from sqlmodel import SQLModel, Field
from datetime import date
from ..enums import SexEnum, ProvinceEnum

class LicenseApplicationBase(SQLModel):
    last_name: str = Field(
        min_length=1,
        max_length=50,
        description="Last name of applicant",
        index=True
    )
    first_name: str = Field(
        min_length=1,
        max_length=50,
        description="First name of applicant",
        index=True
    )
    middle_name: Optional[str] = Field(
        default=None,
        max_length=50,
        description="Middle name of applicant"
    )
    license_number: str = Field(
        description="Driver's license number",
        unique=True,
        index=True,
        sa_column_kwargs={"unique": True}
    )
    date_of_birth: date = Field(
        description="Date of birth of applicant"
    )
    sex: SexEnum = Field(
        description="Biological sex of applicant"
    )
    height_cm: int = Field(
        description="Height of applicant in centimeters",
        gt=50,
        lt=300
    )
    residential_address: str = Field(
        min_length=5,
        max_length=200,
        description="Residential address of applicant"
    )
    mailing_address: str = Field(
        min_length=5,
        max_length=200,
        description="Mailing address of applicant"
    )
    province: ProvinceEnum = Field(
        description="Province of applicant"
    )
    postal_code: str = Field(
        max_length=7,
        description="Postal code of applicant"
    )

class LicenseApplication(LicenseApplicationBase, table=True):
    """Database model for license applications"""
    __tablename__ = "license_applications"
    
    id: Optional[int] = Field(default=None, primary_key=True)


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