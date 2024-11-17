
from fastapi import FastAPI
from app.routers import drivers_license
from app.database import Base, engine
from app import crud

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include routes
app.include_router(drivers_license.router, prefix="/api")

print("main.py loaded")
