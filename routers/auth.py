from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
import database, models.user as models, auth.jwt_handler as jwt_handler

router = APIRouter(tags=["Auth"])

@router.post("/register")
def register(username: str, password: str, db: Session = Depends(database.get_db)):
    # Cek apakah user sudah ada
    user_exists = db.query(models.User).filter(models.User.username == username).first()
    if user_exists:
        raise HTTPException(status_code=400, detail="Username sudah terdaftar")
    
    new_user = models.User(username=username, hashed_password=jwt_handler.hash_password(password))
    db.add(new_user)
    db.commit()
    return {"message": "User berhasil didaftarkan"}

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.username == form_data.username).first()
    if not user or not jwt_handler.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Username atau password salah")
    
    access_token = jwt_handler.create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}