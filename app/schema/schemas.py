from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from pydantic import BaseModel, Field, constr, conint
from datetime import date
from typing import Optional



'base class - contains all fields in application form'
class LicenseApplicationBase(BaseModel):
    last_name: constr (min_length=1, max_length=50, strip_whitespace=True) = Field(
        description="Last name of applicant (1-50 characters)",
        examples=["Smith"]
    )
    first_name: constr(min_length=1, max_length=50, strip_whitespace=True) = Field(
        description="First name of applicant (1-50 characters)",
        examples=["John"]
    )
    middle_name: Optional[constr(max_length=50, strip_whitespace=True)] = Field(
        default=None,
        description="Middle name of applicant (optional, max 50 characters)",
        examples=["Robert"]
    )
    license_number: constr(regex="^[A-Z]{2}[0-9]{6}$") = Field(
        description="Driver's license number in format XX123456",
        examples=["AB123456"]
    )
    date_of_birth: date = Field(
        description="Date of birth of applicant (YYYY-MM-DD)",
        examples=["1990-01-01"]
    )
    sex: SexEnum = Field(
        description="Biological sex of applicant",
        examples=["male"]
    )
    height_cm: conint(ge=50, le=300) = Field(
        description="Height of applicant in centimeters (50-300cm)",
        examples=[175]
    )
    residential_address: constr(min_length=5, max_length=200, strip_whitespace=True) = Field(
        description="Residential address of applicant (5-200 characters)",
        examples=["123 Main Street, Apartment 4B"]
    )
    mailing_address: constr(min_length=5, max_length=200, strip_whitespace=True) = Field(
        description="Mailing address of applicant (5-200 characters)",
        examples=["123 Main Street, Apartment 4B"]
    )
    province: ProvinceEnum = Field(
        description="Province of applicant",
        examples=["Ontario"]
    )
    postal_code: constr(regex="^[A-Z][0-9][A-Z]\s?[0-9][A-Z][0-9]$", strip_whitespace=True) = Field(
        description="Postal code in Canadian format (A1A 1A1)",
        examples=["A1B 2C3"]
    )

    model_config = ConfigDict(from_attributes=True)

class CreateApplication(LicenseApplicationBase):
    pass

'output class-goes into database, needs ID'
class LicenseApplications(LicenseApplicationBase):
    id: int

connect_args = {"check_same_thread": False}

model_config = {
        "from_attributes": True 
    }

"""
Steps to creating schemas:
1. Create base class - class NameBase(BaseModel)
    This contains all the fields in application form

2. Class for user input - this will inherit all the fields from the base class
    class CreateApplication(NameBase)

    used specifically for creating new driver's licenses. The pass statement means it adds no new fields.
3. Class for output - this will inherit all the fields from the base class plus an ID to be stored in database

Notes:
- Schemas are for
    - defining the structure of the data
    - defining constraints
    - It is EVERYTHING DATA
    - error messages are user friendly - with the use of constraints, users can see errors immediately
    - Validate incoming user data (e.g., ensuring correct format, required fields, etc.).
    - Add stricter constraints that aren't enforced at the database level (e.g., regex for postal codes).


"""