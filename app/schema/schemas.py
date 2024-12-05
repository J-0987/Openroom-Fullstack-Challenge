
from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import date, datetime
from typing import Optional

#Create draft application
class LicenseApplicationCreate(SQLModel):
    """Schema for creating a new license application"""
   
    last_name: str
    first_name: str
    license_number: Optional[str] = None
    date_of_birth: Optional[date] = None
    sex: Optional[str] = None
    height_cm: Optional[int] = None
    street_number: Optional[str] = None 
    street_name: Optional[str] = None
    city: Optional[str] = None
    province: Optional[str] = None
    postal_code: Optional[str] = None
    

#Edit draft application
class LicenseApplicationEdit(SQLModel):
    """Schema for updating an existing license application"""
    id: int
    last_name: Optional[str] = None
    first_name: Optional[str] = None
    middle_name: Optional[str] = None
    license_number: Optional[str] = None
    date_of_birth: Optional[date] = None
    sex: Optional[str] = None
    height_cm: Optional[int] = None
    street_number: Optional[str] = None 
    street_name: Optional[str] = None
    city: Optional[str] = None
    province: Optional[str] = None
    postal_code: Optional[str] = None
    status: Optional[str] = None

#Submit application
class LicenseApplicationSubmit(SQLModel):
    """Schema for submitting a license application"""
    id: Optional[int] = None
    last_name: str
    first_name: str
    license_number: str
    date_of_birth: date
    sex: str
    height_cm: int
    street_number: Optional[str] = None 
    street_name: Optional[str] = None
    city: Optional[str] = None
    province: Optional[str] = None
    postal_code: Optional[str] = None



class LicenseApplicationResponse(SQLModel):
     """Schema for responding with license application data"""
     id: int
     last_name: Optional[str] = None
     first_name: Optional[str] = None
     middle_name: Optional[str] = None
     license_number: Optional[str] = None
     date_of_birth: Optional[date] = None
     sex: Optional[str] = None
     height_cm: Optional[int] = None
     street_number: Optional[str] = None 
     street_name: Optional[str] = None
     city: Optional[str] = None
     province: Optional[str] = None
     postal_code: Optional[str] = None
     

    
class LicenseApplicationList(SQLModel):
    """Schema for listing all applications"""
    id: int
    last_name: Optional[str] = None
    first_name: Optional[str] = None
    status: str
    created_at: datetime


"""
Steps to creating schemas:
1. Create base class - class NameBase(BaseModel)
    This contains all the fields in application form

2. Class for user input - this will inherit all the fields from the base class
    class CreateApplication(NameBase)

    used specifically for creating new driver's licenses. The pass statement means it adds no new fields.
3. Class for output - this will inherit all the fields from the base class plus an ID to be stored in database


4. Schemas are for
    - defining the structure of the data
    - defining constraints
    - It is EVERYTHING DATA
    - error messages are user friendly - with the use of constraints, users can see errors immediately
    - Validate incoming user data (e.g., ensuring correct format, required fields, etc.).
    - Add stricter constraints that aren't enforced at the database level (e.g., regex for postal codes).

Notes
   To allow for save functionlity, I am trialling 2 ways 
    1. Create partial schemas with all fields as optional
        ??How do I ensure both schemas will be in the same table?
    2. Create a base schema with all fields as optional, add validations before submitting. Each will be accompanied by status - "draft and submitted"
Output Schemas
1. For data coming out of database
2. Allows customisation of output data

Debugging when created application list:

Error: Trying to get all appplications, even thouse with incomplete fields. My list scehma was first inherited from license application base, which had all fields. I had to create a new schema with only the ID and status. HEre's why:
    Derived Classes: If you create another schema (LicenseApplicationList) that inherits from LicenseApplicationBase, by default, all the fields in the base class are inherited unless explicitly modified or removed.

    The error occurs because the GET endpoint is trying to serialize an instance of LicenseApplication into a response using the LicenseApplicationList schema, but some fields (sex and height_cm) have None values, which the response validator still expects.

    Even though you've commented out the fields, the inheritance still includes them unless they are explicitly removed or overridden. Pydantic is attempting to validate all inherited fields, regardless of whether they are commented out.



"""