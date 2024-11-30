from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, Annotated
from pydantic import BaseModel, Field, constr, conint
from datetime import date
from typing import Optional
from enum import Enum
'base class - contains all fields in application form'

# Base class for license
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
        pattern="^[A-Z][0-9]{14}$",
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
    status: str = Field(
        default="draft",
        description="Application status",
        examples=["draft", "submitted"]
    )

## Schema for submitted applications
class SubmitApplication(LicenseApplicationBase):
    """Schema for final submission with required fields and validations"""

    last_name: str = Field(..., description="Required: Applicant's legal last name")
    first_name: str = Field(..., description="Required: Applicant's legal first name")
    license_number: str = Field(..., description="Required: Driver's license number")
    date_of_birth: date = Field(..., description="Required: Date of birth")
    sex: str = Field(..., description="Required: Biological sex")
    height_cm: int = Field(..., description="Required: Height in centimeters")
    residential_address: str = Field(..., description="Required: Current address")
    province: str = Field(..., description="Required: Province of residence")
    postal_code: str = Field(..., description="Required: Postal code")
    status: str = Field(default="submitted", description="Application status")

    """ In Pydantic, Field(...) means the field is required and has no default value1. The ellipsis (...) is Python's way of indicating a required value without a default."""
 

## Response schema for saved applications
class LicenseApplicationResponse(LicenseApplicationBase):
    """Schema for license application with database ID"""
    id: int = Field(description="Unique identifier for the application")

class LicenseApplicationList(LicenseApplicationBase):
    """Schema for license application with database ID"""
    id: int
    first_name: Optional[str]
    last_name: Optional[str]
    license_number: Optional[str]
    status: str

model_config = ConfigDict(from_attributes=True)

"""
Steps to creating schemas:
1. Create base class - class NameBase(BaseModel)
    This contains all the fields in application form

2. Class for user input - this will inherit all the fields from the base class
    class CreateApplication(NameBase)

    used specifically for creating new driver's licenses. The pass statement means it adds no new fields.
3. Class for output - this will inherit all the fields from the base class plus an ID to be stored in database


4. Schemas are for
    - defining the structure of the data
    - defining constraints
    - It is EVERYTHING DATA
    - error messages are user friendly - with the use of constraints, users can see errors immediately
    - Validate incoming user data (e.g., ensuring correct format, required fields, etc.).
    - Add stricter constraints that aren't enforced at the database level (e.g., regex for postal codes).

Notes
   To allow for save functionlity, I am trialling 2 ways 
    1. Create partial schemas with all fields as optional
        ??How do I ensure both schemas will be in the same table?
    2. Create a base schema with all fields as optional, add validations before submitting. Each will be accompanied by status - "draft and submitted"



"""