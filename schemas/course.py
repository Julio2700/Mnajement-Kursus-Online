from pydantic import BaseModel
from typing import List, Optional

# Skema dasar untuk Lesson
class LessonBase(BaseModel):
    title: str
    content: str

class LessonCreate(LessonBase):
    course_id: int

class Lesson(LessonBase):
    id: int
    
    class Config:
        from_attributes = True

# Skema dasar untuk Course
class CourseBase(BaseModel):
    title: str
    description: str

class CourseCreate(CourseBase):
    pass

class Course(CourseBase):
    id: int
    lessons: List[Lesson] = [] # Menampilkan daftar lesson di dalam detail course 

    class Config:
        from_attributes = True