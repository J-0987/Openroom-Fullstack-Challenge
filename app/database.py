from sqlmodel import create_engine, Session
from sqlalchemy import text
from typing import Generator
import os
from dotenv import load_dotenv

load_dotenv()

# Database URL configuration
DATABASE_URL = os.getenv("DATABASE_URL")

# Create engine with proper configuration for PostgreSQL
engine = create_engine(
    DATABASE_URL,
    echo=True,  # Set to False in production
    isolation_level="AUTOCOMMIT"
  
)
print(f"DATABASE_URL: {DATABASE_URL}")


# Session dependency
def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session


