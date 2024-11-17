from fastapi import Depends
from sqlalchemy.orm import Session
from .models import DriverLicenseApplication
from .schemas import DriverLicenseCreate
from .main import app 

def create_driver_license(db: Session, license_data: DriverLicenseCreate):
    db_license = DriverLicenseApplication(**license_data.dict())
    db.add(db_license)
    db.commit()
    db.refresh(db_license)
    return db_license


def get_driver_licenses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(DriverLicenseApplication).offset(skip).limit(limit).all()

def delete_driver_license(db: Session, license_id: int):
    db_license = db.query(DriverLicenseApplication).filter(DriverLicenseApplication.id == license_id).first()
    db.delete(db_license)
    db.commit()
    return db_license