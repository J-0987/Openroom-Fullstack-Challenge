from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.models import LicenseApplication
from app.schema import CreateDraft, SubmitApplication, LicenseApplicationResponse, LicenseApplicationList
from app.database import get_session
from app.crud import save_draft, submit_application, get_all_applications, get_application_by_id, delete_application, submit_draft_application, edit_draft
from typing import List


router = APIRouter()


@router.post("/applications/draft/", response_model=LicenseApplicationResponse)
async def save_application_draft(data: CreateDraft, session: Session = Depends(get_session)):

    draft = save_draft(session, data)
    # Return the response using the response model to ensure it matches the expected format
    # response = LicenseApplicationResponse(draft)
    return draft


#Update/Edit an existing draft
@router.put("/applications/edit/{application_id}", response_model=LicenseApplicationResponse)
def update_application_draft(application_id: int, data: CreateDraft, session: Session = Depends(get_session)):
    return edit_draft(session, application_id, data)

#submit a completed draft form 
@router.post("/applications/submit/{application_id}", response_model=LicenseApplicationResponse)
def submit_draft_form(application_id: int, data: SubmitApplication, session: Session = Depends(get_session)):
   application = submit_draft_application(session, application_id, data)    
   application.status = "submitted"
   return application

#submit a completed form 
@router.post("/applications/complete/submit/", response_model=LicenseApplicationResponse)
def submit_complete_application(data: SubmitApplication, session: Session = Depends(get_session)):
    return submit_application(session, data)    


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


#View a specific form (GET)
@router.get("/applications/{application_id}", response_model=LicenseApplicationResponse)
def view_specific_form(application_id: int, session: Session = Depends(get_session)):
    return get_application_by_id(session, application_id)

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