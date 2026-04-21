from fastapi import FastAPI
import database, models.course as models
from routers import course, lesson 
from routers import course, lesson, auth

app = FastAPI(
    title="LMS Microservice API",
    description="API untuk Manajemen Kursus Online - UTS Pemrograman Web Lanjutan",
    version="1.0.0"
)

models.Base.metadata.create_all(bind=database.engine)

app.include_router(course.router)
app.include_router(lesson.router)
app.include_router(auth.router)
app.include_router(course.router)
app.include_router(lesson.router)

@app.get("/")
def read_root():
    return {"message": "Selamat Datang di API Manajemen Kursus Online, PAK BOS JULL!"}

