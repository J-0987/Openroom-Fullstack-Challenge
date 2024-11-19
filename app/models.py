from sqlmodel import SQLModel, Field
from datetime import date
from typing import Optional

class DriverLicenseApplication(SQLModel, table=True):
    __tablename__ = "license_applications"

    id: int = Field(default=None, primary_key=True)
    last_name: str
    first_name: str
    middle_name: Optional[str] = None
    license_number: str = Field(unique=True)
    date_of_birth: date
    sex: str
    height_cm: int
    residential_address: str
    mailing_address: str
    province: str
    postal_code: str

print("models.py loaded")


'''
Notes
- Field used in schemas serve the purpose of serialization (how data is shown in console for eg) and 
'''