from fastapi import FastAPI
import database

app = FastAPI(
    title="LMS Microservice API",
    description="API untuk Manajemen Kursus Online - UTS Pemrograman Web Lanjutan",
    version="1.0.0"
)

# Membuat tabel di database saat aplikasi dijalankan
database.Base.metadata.create_all(bind=database.engine)

@app.get("/")
def read_root():
    return {"message": "Selamat Datang di API Manajemen Kursus Online, PAK BOS JULL!"}

@app.get("/health")
def health_check():
    return {"status": "Aplikasi Berjalan Lancar"}