from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth")


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    if token == "QnPwuUSCTmi4X6f9m9FQldBKjzuiChhRIm1pETW3p23MAuh7Zftt0cbs5p90IM6v":
        return True
    else:
        raise credentials_exception
