from typing import Optional
from sqlmodel import SQLModel, Field
from datetime import date, datetime

class LicenseApplicationBase(SQLModel):
    """Database model for license applications"""


    last_name: Optional[str] = Field(
        default=None,
        max_length=50,
        description="Last name of applicant"
    )
    first_name: Optional[str] = Field(
        default=None,
        max_length=50,
        description="First name of applicant"
    )
    middle_name: Optional[str] = Field(
        default=None,
        max_length=50,
        description="Middle name of applicant"
    )
    license_number: Optional[str] = Field(
        default=None,
        unique=True,
        index=True,
        description="Driver's license number"
    )
    date_of_birth: Optional[date] = Field(
        default=None,
        description="Date of birth of applicant"
    )
    sex: Optional[str] = Field(
        default=None,
        description="Biological sex of applicant"
    )
    height_cm: Optional[int] = Field(
        default=None,
        description="Height of applicant in centimeters"
    )
    unit_number: Optional[int] = Field(
        default=None,
        description="Unit number of applicant"
    )
    street_number: Optional[int] = Field(
        default=None,
        description="Street number of applicant"
    )
    street_name: Optional[str] = Field(
        default=None,
        description="Street name of applicant"
    )
    city: Optional[str] = Field(
        default=None,
        description="City of applicant"
    )
    province: Optional[str] = Field(
        default=None,
        description="Province of applicant"
    )
    postal_code: Optional[str] = Field(
        default=None,
        description="Postal code"
    )
    status: str = Field(
        default="draft",
        index=True,
        description="Application status (draft or submitted)"
    )
 
class LicenseApplication(LicenseApplicationBase, table=True):
    """Database model for license applications"""
    __tablename__ = "license_applications"

    id: Optional[int] = Field(default=None, primary_key=True, description="Unique identifier for the application")
    created_at: datetime = Field(default_factory=datetime.utcnow, description="Timestamp of application creation")
    status: str = Field(default="draft", description="Status of the application")


