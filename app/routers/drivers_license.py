from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas, models
from app.database import SessionLocal

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/driver-license/", response_model=schemas.DriverLicense)
def create_license(license_data: schemas.DriverLicenseCreate, db: Session = Depends(get_db)):
    return{"message": "Fetching driver licenses"}
    # return crud.create_driver_license(db=db, license_data=license_data)

@router.get("/driver-license/", response_model=list[schemas.DriverLicense])
def read_licenses(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_driver_licenses(db=db, skip=skip, limit=limit)
