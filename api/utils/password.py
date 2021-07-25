import data.users as data
from typing import Optional

from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext
from constants import PASSWORD_KEY, SECRET_KEY, ALGORITHM

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_hash(password):
    return pwd_context.hash(password)


def authenticate(username: str, password: str):
    user = data.get_user(username)
    if not user:
        return False
    if not verify(password, user[PASSWORD_KEY]):
        return False
    return user


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt