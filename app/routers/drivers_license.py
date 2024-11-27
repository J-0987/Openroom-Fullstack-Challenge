from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session  
from typing import List
from app import crud, schemas, models
from app.database import get_session 


router = APIRouter()


@router.get("/driver-license/", response_model=List[schemas.LicenseApplicationList])
def read_license(skip: int = 0, limit: int = 19, db: Session = Depends(get_session)):
    try:
        licenses = crud.get_driver_licenses(db, skip=skip, limit=limit)
        # Convert SQLModel objects to Pydantic models
        return [schemas.LicenseApplicationList.model_validate(license.model_dump(mode="json")) for license in licenses]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
            

@router.post("/driver-license/", response_model=schemas.CreateApplication)
def create_application(license_data: schemas.CreateApplication, db: Session = Depends(get_session)):
    try:
        return crud.create_application(db=db, license_data=license_data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/driver-license/{license_id}", response_model=schemas.LicenseApplicationList)
def read_license(license_id: int, db: Session = Depends(get_session)):
    db_license = crud.get_driver_licenses(db=db, license_id=license_id)
    if db_license is None:
        raise HTTPException(status_code=404, detail="License not found")
    return db_license


@router.delete("/driver-license/{license_id}", response_model=schemas.LicenseApplicationList)
def delete_license(license_id: int, db: Session = Depends(get_session)):
    db_license = crud.delete_driver_license(db=db, license_id=license_id)
    if db_license is None:
        raise HTTPException(status_code=404, detail="License not found")
    return


