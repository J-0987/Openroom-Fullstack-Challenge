import logging
from fastapi import FastAPI
from app.routers import drivers_license
from app.database import  engine
from app import crud
from typing import Union
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import SQLModel


# Create tables
SQLModel.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost:3000",  
    "http://127.0.0.1:3000",  
    "localhost:3000",         
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

import logging

logging.basicConfig(level=logging.DEBUG)
logging.debug("main.py loaded")
print("main.py loaded")