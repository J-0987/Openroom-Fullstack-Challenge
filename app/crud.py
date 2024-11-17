from sqlalchemy.orm import Session
from .models import DriverLicenseApplication
from .schemas import DriverLicenseCreate

def create_driver_license(db: Session, license_data: DriverLicenseCreate):
    db_license = DriverLicenseApplication(**license_data.dict())
    db.add(db_license)
    db.commit()
    db.refresh(db_license)
    return db_license
