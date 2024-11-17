from pydantic import BaseModel, Field
from datetime import date

class DriverLicenseBase(BaseModel):
    last_name: str
    first_name: str
    middle_name: str = None
    license_number: str = None
    date_of_birth: date
    sex: str
    height_cm: int
    residential_address: str
    mailing_address: str = None
    province: str
    postal_code: str

class DriverLicenseCreate(DriverLicenseBase):
    pass

class DriverLicense(DriverLicenseBase):
    id: int

    class Config:
        orm_mode = True
