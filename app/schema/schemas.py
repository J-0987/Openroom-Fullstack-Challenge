from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, Annotated
from pydantic import BaseModel, Field, constr, conint
from datetime import date
from typing import Optional
from ..enums import SexEnum, ProvinceEnum

'base class - contains all fields in application form'

# Completed application schema
class LicenseApplicationBase(BaseModel):

    last_name: Annotated[str, Field(
        min_length=1, 
        max_length=50,
        description="Last name of applicant (1-50 characters)",
        examples=["Smith"]
    )]
    first_name: Annotated[str, Field(
        min_length=1,
        max_length=50,
        description="First name of applicant (1-50 characters)",
        examples=["John"]
    )]
    middle_name: Optional[Annotated[str, Field(
        max_length=50,
        default=None,
        description="Middle name of applicant (optional, max 50 characters)",
        examples=["Robert"]
    )]]
    license_number: Annotated[str, Field(
        pattern="^[A-Za-z0-9]*$",
        description="Driver's license number in format XX123456",
        examples=["AB123456"]
    )]
    date_of_birth: date = Field(
        description="Date of birth of applicant (YYYY-MM-DD)",
        examples=["1990-01-01"]
    )
    sex: Annotated[str, Field(
        description="Biological sex of applicant",
        examples=["male"]
    )]
    height_cm: Annotated[int, Field(
        ge=50,
        le=300,
        description="Height of applicant in centimeters (50-300cm)",
        examples=[175]
    )]
    residential_address: Annotated[str, Field(
        min_length=5,
        max_length=200,
        description="Residential address of applicant (5-200 characters)",
        examples=["123 Main Street, Apartment 4B"]
    )]
    
    province: Annotated [str, Field(
        description="Province of applicant",
        examples=["Ontario"]
    )]
    postal_code: Annotated[str, Field(
        pattern="^[A-Za-z0-9]*$",
        description="Postal code in Canadian format (A1A 1A1)",
        examples=["A1B 2C3"]
    )]

# Partial application schema
class LicenseApplicationSave(BaseModel):
    last_name: Optional[str]
    first_name: Optional[str]
    middle_name: Optional[str]
    license_number: Optional[str]
    date_of_birth: Optional[date]
    sex: Optional[str]
    height_cm: Optional[int]
    residential_address: Optional[str]
    province: Optional[str]
    postal_code: Optional[str]


model_config = ConfigDict(from_attributes=True)

class CreateApplication(LicenseApplicationBase):
    """Schema for creating a new license application"""
    pass

class LicenseApplicationList(LicenseApplicationBase):
    """Schema for license application with database ID"""
    id: int = Field(description="Unique identifier for the application")



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