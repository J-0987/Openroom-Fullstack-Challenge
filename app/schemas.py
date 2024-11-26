from pydantic import BaseModel, Field, ConfigDict
from datetime import date
from typing import Optional



'base class - contains all fields in application form'
class LicenseApplicationBase(BaseModel):
    last_name: str = Field( description="Last name of applicant")
    first_name: str = Field( description="First name of applicant")
    middle_name: Optional[str] = Field(default=None, description="Middle name of applicant")
    license_number: str = Field(description="Driver's license number",pattern="^[A-Z]{2}[0-9]{6}$")
    date_of_birth: date = Field(description="Date of birth of applicant")
    sex: str = Field(description = "biological sex of applicant")
    height_cm: int = Field(description="Height of applicant in cm")
    residential_address: str = Field(description="Residential address of applicant")
    mailing_address: str = Field(description="Mailing address of applicant")
    province: str = Field(description="Province of applicant")
    postal_code: str = Field(description="Postal code of applicant")

    model_config = ConfigDict(from_attributes=True)

class CreateApplication(LicenseApplicationBase):
    pass

'output class-goes into database, needs ID'
class LicenseApplications(LicenseApplicationBase):
    id: int

connect_args = {"check_same_thread": False}

"""
Steps to creating schemas:
1. Create base class - class NameBase(BaseModel)
    This contains all the fields in application form

2. Class for user input - this will inherit all the fields from the base class
    class CreateApplication(NameBase)

    used specifically for creating new driver's licenses. The pass statement means it adds no new fields.
3. Class for output - this will inherit all the fields from the base class plus an ID to be stored in database

Notes:
- Field used in schemas serve the purpose of serialization (how data is shown in console for eg) and Input validation

"""