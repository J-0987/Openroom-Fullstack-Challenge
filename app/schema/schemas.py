from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, Annotated
from pydantic import BaseModel, Field, constr, conint
from datetime import date, datetime
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
        pattern="^*",
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
        pattern="^*",
        description="Postal code in Canadian format (A1A 1A1)",
        examples=["A1B 2C3"]
    )]
    status: Optional[str] = Field(
        default="draft",
        description="Application status (draft or submitted)",
        examples=["draft"]
    )
    
    

## Schema for submitted applications
class SubmitApplication(LicenseApplicationBase):
    """Schema for final submission with required fields and validations"""
    pass

class CreateDraft(LicenseApplicationBase):
    last_name: Optional[str] = None
    first_name: Optional[str] = None
    middle_name: Optional[str] = None
    license_number: Optional[str] = None
    date_of_birth: Optional[date] = None
    sex: Optional[str] = None
    height_cm: Optional[int] = None
    residential_address: Optional[str] = None
    province: Optional[str] = None
    postal_code: Optional[str] = None
    status: str = Field(default="draft", description="Application status")

## Response/output schema (see notes)
class LicenseApplicationResponse(LicenseApplicationBase):
    """Schema for license application with database ID"""
    id: int = Field(description="Unique identifier for the application")
    created_at: datetime

class LicenseApplicationList(BaseModel):
    """Schema for license application with database ID. I am using basemodel to create a schema with only the ID and status"""
    id: int
    last_name: Optional[str] = None
    first_name: Optional[str] = None
    middle_name: Optional[str] = None
    license_number: Optional[str] = None
    date_of_birth: Optional[date] = None
    sex: Optional[str] = None
    height_cm: Optional[int] = None
    residential_address: Optional[str] = None
    province: Optional[str] = None
    postal_code: Optional[str] = None
    created_at: datetime
    status: str

model_config = ConfigDict(from_attributes=True)


## Schema for draft applications
# class CreateDraft(BaseModel):

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
Output Schemas
1. For data coming out of database
2. Allows customisation of output data

Debugging when created application list:

Error: Trying to get all appplications, even thouse with incomplete fields. My list scehma was first inherited from license application base, which had all fields. I had to create a new schema with only the ID and status. HEre's why:
    Derived Classes: If you create another schema (LicenseApplicationList) that inherits from LicenseApplicationBase, by default, all the fields in the base class are inherited unless explicitly modified or removed.

    The error occurs because the GET endpoint is trying to serialize an instance of LicenseApplication into a response using the LicenseApplicationList schema, but some fields (sex and height_cm) have None values, which the response validator still expects.

    Even though you've commented out the fields, the inheritance still includes them unless they are explicitly removed or overridden. Pydantic is attempting to validate all inherited fields, regardless of whether they are commented out.



"""