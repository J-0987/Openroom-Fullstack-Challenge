from fastapi import Depends
from sqlmodel import Session, select
from .models import DriverLicenseApplication
from .schemas import CreateApplication

def create_application(db: Session, license_data: CreateApplication):
    db_license = DriverLicenseApplication.model_validate(license_data)
    db.add(db_license)
    db.commit()
    db.refresh(db_license)
    return db_license


def get_driver_licenses(db: Session, skip: int = 0, limit: int = 100):
    statement = select(DriverLicenseApplication).offset(skip).limit(limit)
    return db.exec(statement).all()

def delete_application(db: Session, license_id: int):
    statement = select(DriverLicenseApplication). where(DriverLicenseApplication.id == license_id)
    db_license = db.exec(statement).first()
    db.delete(db_license)
    db.commit()