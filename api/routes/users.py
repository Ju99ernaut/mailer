import os
import data.users as data
from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, Path, status
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import RedirectResponse
from models import Token, User, UserInDB, UpdateUser, RegisterUser, Message
from dependencies import get_current_user, current_user_is_active, get_email
from utils.password import authenticate, create_access_token, get_hash
from mail.send import user as send_email

from constants import (
    USERNAME_KEY,
    EMAIL_KEY,
    PASSWORD_KEY,
    ACTIVE_KEY,
    ACCESS_TOKEN_EXPIRE_MINUTES,
)
import config

router = APIRouter(tags=["users"], responses={404: {"description": "Not found"}})


@router.post("/register", response_model=User)
async def register_user(user: RegisterUser):
    if data.get_user(user.username):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with same username already exists",
        )
    if data.get_user_by_email(user.email):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="This email already has an account",
        )
    data.add_user(user.username, user.email, get_hash(user.password))
    return_user = data.get_user(user.username)
    if not return_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item not found, failed to register",
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    confirm_token = create_access_token(
        data={"sub": user[EMAIL_KEY]}, expires_delta=access_token_expires
    )
    backend = os.getenv("BACKEND_URL") or config.CONFIG.backend
    if backend:
        await send_email(
            user[EMAIL_KEY],
            {
                "username": user[USERNAME_KEY],
                "confirm_url": f"{backend}/confirm/{confirm_token}",
            },
        )
    return return_user


@router.post("/auth", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user[USERNAME_KEY]}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer", "expires_in": 3600}


@router.get("/confirm/{token}")
async def confirm_email_token(
    token: str = Path(..., description="Token to confirm email")
):
    frontend = os.getenv("FRONTEND_URL") or config.CONFIG.frontend
    email = await get_email(token)
    if not frontend:
        return {"msg": "No frontend to redirect to"}
    if email == "expired":
        return RedirectResponse(url=f"{frontend}/?status=expired")
    user = data.get_user_by_email(email)
    if user:
        data.activate_user(user["id"], {ACTIVE_KEY: True})
        return RedirectResponse(url=f"{frontend}#status=confirmed")
    else:
        return RedirectResponse(url=f"{frontend}#status=unconfirmed")


@router.get("/resend", response_model=Message)
async def regenerate_confirm_email(user: User = Depends(get_current_user)):
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    confirm_token = create_access_token(
        data={"sub": user[EMAIL_KEY]}, expires_delta=access_token_expires
    )
    backend = os.getenv("BACKEND_URL") or config.CONFIG.backend
    if backend:
        await send_email(
            user[EMAIL_KEY],
            {
                "username": user[USERNAME_KEY],
                "confirm_url": f"{backend}/confirm/{confirm_token}",
            },
        )
    return {"msg": "resent"}


@router.put("/users/me", response_model=User)
async def update_user_me(
    user: UpdateUser, current_user: User = Depends(current_user_is_active)
):
    if data.get_user(user.username):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with same username already exists",
        )
    db_user = data.get_user(current_user[USERNAME_KEY])
    data.update_user(db_user["id"], user)
    return data.get_user(user.username or current_user[USERNAME_KEY])


@router.get("/users/me", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user


@router.delete("/users/me", response_model=Message)
async def unregister_users_me(current_user: UserInDB = Depends(get_current_user)):
    data.remove_user(
        current_user[USERNAME_KEY], current_user[EMAIL_KEY], current_user[PASSWORD_KEY]
    )
    if data.get_user(current_user[USERNAME_KEY]):
        raise HTTPException(
            status_code=status.HTTP_417_EXPECTATION_FAILED, detail="Failed to delete"
        )
    return {"msg": "deleted"}
