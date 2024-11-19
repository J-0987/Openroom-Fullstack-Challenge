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

@router.get("/driver-license/", response_model=schemas.DriverLicense)
def read_license(skip: int = 0, limit: int = 19, db: Session = Depends(get_db)):
    licenses = crud.get_driver_licenses(db, skip=skip, limit=limit)
    return {licenses}
            

@router.post("/driver-license/", response_model=schemas.DriverLicense)
def create_license(license_data: schemas.DriverLicenseCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_driver_license(db=db, license_data=license_data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/driver-license/{license_id}", response_model=schemas.DriverLicense)
def read_license(license_id: int, db: Session = Depends(get_db)):
    db_license = crud.get_driver_license(db=db, license_id=license_id)
    if db_license is None:
        raise HTTPException(status_code=404, detail="License not found")
    return db_license


@router.delete("/driver-license/{license_id}", response_model=schemas.DriverLicense)
def delete_license(license_id: int, db: Session = Depends(get_db)):
    db_license = crud.delete_driver_license(db=db, license_id=license_id)
    if db_license is None:
        raise HTTPException(status_code=404, detail="License not found")
    return db_licen

