from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.models import LicenseApplication
from app.schema import LicenseApplicationCreate, LicenseApplicationResponse, LicenseApplicationList, LicenseApplicationEdit, LicenseApplicationSubmit
from app.database import get_session
from app.crud import delete_application, get_application_by_id, get_all_applications, create_draft, edit_draft, submit_application
from typing import List

router = APIRouter()

#Create application
@router.post("/applications/", response_model=LicenseApplicationResponse)
def create_application(data: LicenseApplicationCreate , session: Session = Depends(get_session)):
    application = LicenseApplication(**data.model_dump())

    session.add(application)
    session.commit()
    session.refresh(application)
    return application

#Update/Edit application
@router.patch("/applications/{application_id}", response_model=LicenseApplicationResponse)
def edit_application(application_id: int, updates: LicenseApplicationEdit, session: Session = Depends(get_session)):
    application = session.get(LicenseApplication, application_id)
    if not application:
        raise HTTPException(status_code=404, detail="Application not found")
    for key, value in updates.model_dump(exclude_unset=True).items():
        setattr(application, key, value)
    session.commit()
    session.refresh(application)
    return application

#submit application
@router.post("/applications/submit", response_model=LicenseApplicationResponse)
def submit_application( data: LicenseApplicationSubmit, session: Session = Depends
(get_session)):
  application = session.get(LicenseApplication, data.id)
  if not application:
        raise HTTPException(status_code=404, detail="Application not found")
  
  missing_fields = [
        field for field, value in data.model_dump().items() if value is None
  ]
  if missing_fields:
        raise HTTPException(
            status_code=400,
            detail=f"Missing required fields: {', '.join(missing_fields)}"
        )
  application.status = "submitted"
  session.add(application)
  session.commit()
  session.refresh(application)
  return application
  
#Get single application
@router.get("/applications/{application_id}", response_model=LicenseApplicationResponse)
def get_application(application_id: int , session: Session = Depends(get_session)):
    application = session.get(LicenseApplication, application_id)
    if not application:
        raise HTTPException(status_code=404, detail="Application not found")
    return application

#List all forms (GET)
@router.get("/applications/", response_model=List[LicenseApplicationList])
def list_all_forms(session: Session = Depends(get_session)):
    try:
        applications = list(session.exec(select(LicenseApplication)))
        print("Retrieved applications:", applications)
        if not applications:
            raise HTTPException(status_code=404, detail="No applications found.")
        return applications
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to retrieve applications.")

#Delete a draft form (DELETE)
@router.delete("/applications/{application_id}")
def delete_draft_form(application_id: int, session: Session = Depends(get_session)):
    return delete_application(session, application_id)


"""
OLD CODE BELOW
"""

#get all applications
# @router.get("/applications", response_model=List[schemas.LicenseApplicationList])
# def read_license(skip: int = 0, limit: int = 19, db: Session = Depends(get_session)):
#     try:
#         licenses = crud.get_driver_licenses(db, skip=skip, limit=limit)
#         # Convert SQLModel objects to Pydantic models
#         return [schemas.LicenseApplicationList.model_validate(license.model_dump(mode="json")) for license in licenses]
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
            

# #
# @router.post("/driver-license/", response_model=schemas.CreateApplication)
# def create_application(license_data: schemas.CreateApplication, db: Session = Depends(get_session)):
#     try:
#         return crud.create_application(db=db, license_data=license_data)
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# @router.get("/driver-license/{license_id}", response_model=schemas.LicenseApplicationList)
# def read_license(license_id: int, db: Session = Depends(get_session)):
#     db_license = crud.get_driver_licenses(db=db, license_id=license_id)
#     if db_license is None:
#         raise HTTPException(status_code=404, detail="License not found")
#     return db_license


# @router.delete("/driver-license/{license_id}", response_model=schemas.LicenseApplicationList)
# def delete_license(license_id: int, db: Session = Depends(get_session)):
#     db_license = crud.delete_driver_license(db=db, license_id=license_id)
#     if db_license is None:
#         raise HTTPException(status_code=404, detail="License not found")
#     return


"""
Save a Draft (POST)
Update a Draft (PUT)
Submit a Completed Form (PUT)
List All Forms (GET)
View a Specific Form (GET)
Delete a Draft Form (DELETE)
"""