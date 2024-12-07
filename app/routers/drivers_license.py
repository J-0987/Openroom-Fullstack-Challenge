from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.models import LicenseApplication
from app.schema import LicenseApplicationCreate, LicenseApplicationResponse, LicenseApplicationList, LicenseApplicationEdit, LicenseApplicationSubmit
from app.database import get_session
from app.crud import delete_application, get_application_by_id, get_all_applications, create_draft, edit_draft, submit_application
from typing import List

router = APIRouter()

#Create application (used at first save )
@router.post("/applications/", response_model=LicenseApplicationResponse)
def create_application(data: LicenseApplicationCreate , session: Session = Depends(get_session)):
    return create_draft(session, data)

#Update/Edit application
@router.patch("/applications/{application_id}", response_model=LicenseApplicationResponse)
def edit_application(application_id: int, updates: LicenseApplicationEdit, session: Session = Depends(get_session)):
    return edit_draft(session, application_id, updates)

#submit application
@router.post("/applications/submit", response_model=LicenseApplicationResponse)
def submit_application(data: LicenseApplicationSubmit, session: Session = Depends(get_session)):
    # Validate required fields first
    missing_fields = [
        field for field, value in data.model_dump().items() 
        if value is None and field != 'id'
    ]
    if missing_fields:
        raise HTTPException(
            status_code=400,
            detail=f"Missing required fields: {', '.join(missing_fields)}"
        )

    try:
        # Create new application if no ID provided
        if not data.id:
            new_application = LicenseApplication(**data.model_dump(exclude={'id'}))
            new_application.status = "submitted"
            session.add(new_application)
        else:
            # Update existing application
            existing_application = session.get(LicenseApplication, data.id)
            if not existing_application:
                raise HTTPException(status_code=404, detail="Application not found")
            
            for key, value in data.model_dump().items():
                setattr(existing_application, key, value)
            existing_application.status = "submitted"
        
        session.commit()
        session.refresh(new_application if not data.id else existing_application)
        return new_application if not data.id else existing_application
        
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    
#Get single application
@router.get("/applications/{application_id}", response_model=LicenseApplicationResponse)
def get_application(application_id: int , session: Session = Depends(get_session)):
    return get_application_by_id(session, application_id)

#List all applications (GET)
@router.get("/applications", response_model=List[LicenseApplicationList])
def list_all_applications(session: Session = Depends(get_session)):
    return get_all_applications(session)


#Delete a draft form (DELETE)
@router.delete("/applications/{application_id}")
def delete_draft_form(application_id: int, session: Session = Depends(get_session)):
    return delete_application(session, application_id)


"""
Save a Draft (POST)
Update a Draft (PUT)
Submit a Completed Form (PUT)
List All Forms (GET)
View a Specific Form (GET)
Delete a Draft Form (DELETE)
"""