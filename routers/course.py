from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import database, models.course as models, schemas.course as schemas
from auth.jwt_handler import get_current_user

router = APIRouter(
    prefix="/courses",
    tags=["Courses"]
)

@router.post("/", response_model=schemas.Course, status_code=201)
def create_course(course: schemas.CourseCreate, db: Session = Depends(database.get_db)):
    db_course = models.Course(title=course.title, description=course.description)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

@router.get("/", response_model=List[schemas.Course])
def read_courses(db: Session = Depends(database.get_db)):
    return db.query(models.Course).all()

@router.get("/{course_id}", response_model=schemas.Course)
def read_course(course_id: int, db: Session = Depends(database.get_db)):
    db_course = db.query(models.Course).filter(models.Course.id == course_id).first()
    if db_course is None:
        raise HTTPException(status_code=404, detail="Kursus tidak ditemukan")
    return db_course

@router.post("/", response_model=schemas.Course, status_code=201)
def create_course(
    course: schemas.CourseCreate, 
    db: Session = Depends(database.get_db),
    current_user: str = Depends(get_current_user) # Endpoint ini sekarang terproteksi!
):
    db_course = models.Course(title=course.title, description=course.description)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course