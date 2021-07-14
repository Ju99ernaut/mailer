import data.users as data
from typing import Optional

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from models import TokenData, User

from constants import SECRET_KEY, ALGORITHM, ACTIVE_KEY, ROLE_KEY

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth")


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = data.get_user(username=token_data.username)
    if user is None:
        raise credentials_exception
    return user


async def get_email(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            return "expired"
        return email
    except JWTError:
        return "expired"


async def current_user_is_active(current_user: User = Depends(get_current_user)):
    if not current_user[ACTIVE_KEY]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Not verified"
        )
    return current_user


async def current_user_is_admin(current_user: User = Depends(get_current_user)):
    if current_user[ROLE_KEY] != "admin":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Not admin")
    return current_user
