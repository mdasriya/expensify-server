from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.modules.auth.auth_schema import UserSignup
from app.modules.auth import auth_service

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/signup")
def signup(user: UserSignup, db: Session = Depends(get_db)):
    try:
        return auth_service.create_user(db, user)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
