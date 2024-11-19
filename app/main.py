

from fastapi import FastAPI
from app.routers import drivers_license
from app.database import Base, engine
from app import crud
from typing import Union
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import SQLModel


# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost:3000",  # React default port
    "localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


# Include routes
app.include_router(drivers_license.router, prefix="/api")

print("main.py loaded")