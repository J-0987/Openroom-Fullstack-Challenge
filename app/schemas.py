from pydantic import BaseModel, Field, ConfigDict
from datetime import date
from typing import Optional



'base class - contains all fields in application form'
class LicenseApplicationBase(BaseModel):
    last_name: str 
    first_name: str 
    middle_name: Optional[str] = None
    license_number: str
    date_of_birth: date
    sex: str
    height_cm: int
    residential_address: str
    mailing_address: str 
    province: str
    postal_code: str

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