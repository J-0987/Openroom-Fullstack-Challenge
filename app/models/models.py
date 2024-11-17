from sqlalchemy import Column, Integer, String, Date

from .models import Base

class DriverLicenseApplication(Base):
    __tablename__ = "driver_license_applications"

    id = Column(Integer, primary_key=True, index=True)
    last_name = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    middle_name = Column(String)
    license_number = Column(String, unique=True)
    date_of_birth = Column(Date, nullable=False)
    sex = Column(String, nullable=False)
    height_cm = Column(Integer, nullable=False)
    residential_address = Column(String, nullable=False)
    mailing_address = Column(String)
    province = Column(String, nullable=False)
    postal_code = Column(String, nullable=False)
