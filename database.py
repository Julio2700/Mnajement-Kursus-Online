from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Membuat file database lokal bernama lms_database.db
SQLALCHEMY_DATABASE_URL = "sqlite:///./lms_database.db"

# Engine untuk berinteraksi dengan database
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Session untuk operasi database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class untuk mendefinisikan model-model database nanti
Base = declarative_base()

# Dependency untuk mendapatkan session database di setiap request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()