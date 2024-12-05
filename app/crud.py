from fastapi import Depends, HTTPException
from sqlmodel import Session, select
from app.models import LicenseApplication
from app.schema import LicenseApplicationCreate, LicenseApplicationResponse, LicenseApplicationEdit, LicenseApplicationList, LicenseApplicationSubmit

# create application
def create_draft(session: Session, data: LicenseApplicationCreate):
    """
    Save a draft license application. Must have Id in the payload. Validate that at least one field is populated, save rest as none
    """
    draft = LicenseApplication(**data.model_dump(), status="draft")
    session.add(draft)
    session.commit()
    session.refresh(draft)
    return draft

# edit application
def edit_draft(session: Session, application_id: int, data: LicenseApplicationEdit):
    """
    Retrieve the draft application by ID and update it with new data.
    """
    # Retrieve the draft application by ID
    draft = session.get(LicenseApplication, application_id)
    
    if not draft or draft.status != "draft":
        raise HTTPException(status_code=404, detail="Draft application not found or not in draft status.")
    
    # Update the draft with new data
    for key, value in data.model_dump().items():
        if value is not None:  # Only update fields that have new values
            setattr(draft, key, value)
    
    session.add(draft)
    session.commit()
    session.refresh(draft)
    
    return draft

#submit application
def submit_application(session: Session, data: LicenseApplicationSubmit):
    """
    Payload should have all the required fields including ID. Validate that all fields are populated. Save to db
    """
    application = LicenseApplication(**data.model_dump(), status="submitted")
    session.add(application)
    session.commit()
    session.refresh(application)
    return application

def get_all_applications(session: Session):
    """
    Retrieve all license applications from the database.
    """
    applications = session.exec(select(LicenseApplication)).all()
    return applications

def get_application_by_id(session: Session, application_id: int):
    """
    Retrieve a specific license application by its ID.
    """
    application = session.get(LicenseApplication, application_id)
    if not application:
        raise HTTPException(status_code=404, detail="Application not found.")
    return application

def delete_application(session: Session, application_id: int):
    """
    Delete a license application by its ID.
    """
    application = session.get(LicenseApplication, application_id)
    if not application:
        raise HTTPException(status_code=404, detail="Application not found.")
    session.delete(application)
    session.commit()
    return {"detail": "Application deleted successfully."}

"""
Notes:
Purpose of this file:
- Using models to interact with the database
- convert incoming data to models 
- convert model to schema when sending data to client
"""