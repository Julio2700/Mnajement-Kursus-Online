````markdown
# LMS Microservice API - UTS Pemrograman Web Lanjutan

Aplikasi Microservice untuk manajemen kursus online (LMS) sederhana yang dibangun menggunakan **FastAPI**, **SQLAlchemy**, dan **JWT Authentication**.

## Fitur Utama
- **CRUD Course & Lesson**: Manajemen data kursus dan materi dengan relasi One-to-Many.
- **JWT Authentication**: Sistem registrasi dan login untuk mendapatkan akses token.
- **Authorization**: Proteksi endpoint sehingga hanya user terdaftar yang bisa menambah data.
- **Dokumentasi Otomatis**: Integrasi Swagger UI untuk pengujian API secara langsung.

## Spesifikasi Teknis
- **Framework**: FastAPI
- **Database**: SQLite (ORM SQLAlchemy)
- **Python Version**: 3.12.6
- **Security**: Passlib (Bcrypt) & Python-Jose (JWT)

## Cara Menjalankan Proyek Lokal

### 1. Clone Repository
```bash
git clone [https://github.com/Julio2700/Mnajement-Kursus-Online.git](https://github.com/Julio2700/Mnajement-Kursus-Online.git)
cd Mnajement-Kursus-Online
````

### 2\. Buat & Aktifkan Virtual Environment

```bash
python -m venv venv
.\venv\Scripts\activate
```

### 3\. Instalasi Dependensi

```bash
pip install -r requirements.txt
```

### 4\. Jalankan Server

```bash
uvicorn main:app --reload
```

### 5\. Akses Dokumentasi

Setelah server berjalan, buka browser dan akses:

  - **Swagger UI**: [http://127.0.0.1:8000/docs](https://www.google.com/search?q=http://127.0.0.1:8000/docs)
  - **ReDoc**: [http://127.0.0.1:8000/redoc](https://www.google.com/search?q=http://127.0.0.1:8000/redoc)