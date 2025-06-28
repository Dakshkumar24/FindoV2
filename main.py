from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, Column, Integer, String, DateTime, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
import os
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Database setup
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./findo.db")

# For SQLite, we need to add check_same_thread=False
if SQLALCHEMY_DATABASE_URL.startswith("sqlite"):
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
    )
else:
    engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Create database tables
def create_tables():
    Base.metadata.create_all(bind=engine)
    
    # Add a test document if the database is empty
    db = SessionLocal()
    try:
        # Check if documents table exists and is empty
        result = db.execute(text("SELECT name FROM sqlite_master WHERE type='table' AND name='documents'"))
        if result.first():
            count = db.execute(text("SELECT COUNT(*) FROM documents")).scalar()
            if count == 0:
                # Add a test document
                db.execute(text(
                    "INSERT INTO documents (title, description, created_at) VALUES (:title, :description, :created_at)"
                ), {"title": "Welcome to FinDo", "description": "This is a test document", "created_at": datetime.utcnow()})
                db.commit()
        else:
            # Create documents table if it doesn't exist
            db.execute(text("""
                CREATE TABLE documents (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    description TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """))
            # Add a test document
            db.execute(text(
                "INSERT INTO documents (title, description, created_at) VALUES (:title, :description, :created_at)"
            ), {"title": "Welcome to FinDo", "description": "This is a test document", "created_at": datetime.utcnow()})
            db.commit()
    except Exception as e:
        print(f"Error initializing database: {e}")
        db.rollback()
    finally:
        db.close()

# Create database tables
create_tables()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Models
class DocumentBase(BaseModel):
    title: str
    description: Optional[str] = None

class DocumentCreate(DocumentBase):
    pass

class Document(DocumentBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

# FastAPI app
app = FastAPI(title="FinDo API", description="Financial Document Organization API", version="1.0.0")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API Routes
@app.get("/")
async def root():
    return {
        "message": "Welcome to FinDo API",
        "status": "running",
        "timestamp": datetime.utcnow().isoformat(),
        "environment": os.getenv("ENV", "development"),
        "database": "SQLite" if "sqlite" in SQLALCHEMY_DATABASE_URL else "PostgreSQL"
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy", "timestamp": datetime.utcnow().isoformat()}

@app.get("/documents/", response_model=List[Document])
def list_documents(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    result = db.execute(text("SELECT * FROM documents ORDER BY created_at DESC LIMIT :limit OFFSET :skip"), 
                       {"limit": limit, "skip": skip})
    documents = [dict(row) for row in result.mappings().all()]
    return documents

@app.post("/documents/", response_model=Document)
def create_document(document: DocumentCreate, db: Session = Depends(get_db)):
    result = db.execute(
        text("""
            INSERT INTO documents (title, description, created_at) 
            VALUES (:title, :description, :created_at)
            RETURNING id, title, description, created_at
        """),
        {"title": document.title, "description": document.description, "created_at": datetime.utcnow()}
    )
    db.commit()
    return result.mappings().first()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
