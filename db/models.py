from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# --- Database (SQLAlchemy) Setup ---

DATABASE_URL = "sqlite:///./poem_project.db"

Base = declarative_base()
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Poem(Base):
    __tablename__ = "poems"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    topic = Column(String)
    poem_text = Column(Text)

# --- API (Pydantic) Models ---

class PoemRequest(BaseModel):
    name: str
    topic: str

class PoemResponse(BaseModel):
    poem: str