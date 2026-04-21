from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import database, models.course as models, schemas.course as schemas

router = APIRouter(
    prefix="/lessons",
    tags=["Lessons"]
)

# Endpoint: Menambahkan Materi ke Kursus tertentu (Create)
@router.post("/", response_model=schemas.Lesson, status_code=201)
def create_lesson(lesson: schemas.LessonCreate, db: Session = Depends(database.get_db)):
    # Validasi: Cek apakah Course ID-nya benar-benar ada
    db_course = db.query(models.Course).filter(models.Course.id == lesson.course_id).first()
    if not db_course:
        raise HTTPException(status_code=404, detail="Course tidak ditemukan, tidak bisa menambah materi")
    
    db_lesson = models.Lesson(**lesson.dict())
    db.add(db_lesson)
    db.commit()
    db.refresh(db_lesson)
    return db_lesson

# Endpoint: Mengambil Semua Materi (Read List)
@router.get("/", response_model=List[schemas.Lesson])
def read_lessons(db: Session = Depends(database.get_db)):
    return db.query(models.Lesson).all()