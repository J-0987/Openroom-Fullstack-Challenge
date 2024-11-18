from pydantic import BaseModel, Field, ConfigDict
from datetime import date
from typing import Annotated

class DriverLicenseBase(BaseModel):
    last_name: str = Field(min_length=2, max_length=50)
    first_name: str = Field(min_length=2, max_length=50)
    middle_name: str | None = None 
    license_number: str
    date_of_birth: date
    sex: str
    height_cm: int
    residential_address: str
    mailing_address: str 
    province: str
    postal_code: str

    model_config = ConfigDict(from_attributes=True)

class DriverLicenseCreate(DriverLicenseBase):
    pass

class DriverLicense(DriverLicenseBase):
    id: int

model_config = ConfigDict(from_attributes=True)
