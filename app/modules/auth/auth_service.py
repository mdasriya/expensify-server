from sqlalchemy.orm import Session
from app.modules.auth.auth_model import User
from app.core.security import hash_password

def create_user(db: Session, user_data):
    existing_user = db.query(User).filter(User.email == user_data.email).first()

    if existing_user:
        raise Exception("Email already registered")

    hashed_pwd = hash_password(user_data.password)

    new_user = User(
        email=user_data.email,
        password=hashed_pwd
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
