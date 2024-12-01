from typing import Optional
from sqlmodel import SQLModel, Field
from datetime import date, datetime

class LicenseApplication(SQLModel, table=True):
    """Database model for license applications"""
    __tablename__ = "license_applications"
    
    # Required fields with validation constraints

    id: Optional[int] = Field(default=None, primary_key=True, description="Unique identifier for the application")

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
    residential_address: Optional[str] = Field(
        default=None,
        max_length=200,
        description="Residential address of applicant"
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
    created_at: datetime = Field(
        default=datetime.now(),
        description="Timestamp of application creation"
    )