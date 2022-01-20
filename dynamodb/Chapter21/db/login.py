from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from pydantic import ValidationError
from typing import Union, Any
from datetime import datetime, timedelta
from fastapi.security import HTTPBearer

import jwt

SECURIT_ALGORITHM = 'HS256'
SECRET_KEY = '123456'

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def verify_password(username, password):
    if username == 'admin' and password == 'admin':
        return True
    return False


def generate_token(username: Union[str, Any]) -> str:
    expire = datetime.utcnow() + timedelta(
        seconds=60 * 60 * 24 * 3  # Expired after 3 days
    )
    to_encode = {
        "exp": expire, "username": username
    }
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY,
                             algorithm=SECURIT_ALGORITHM)
    # First para is payload

    return encoded_jwt


reusable_oauth2 = HTTPBearer(
    scheme_name='Authorization'
)


def validate_token(credentials=Depends(reusable_oauth2)) -> str:
    """
    Decode JWT token
    """
    try:
        payload = jwt.decode(credentials.credentials, SECRET_KEY,
                             algorithms=[SECURIT_ALGORITHM])
        if payload.get('exp') < datetime.utcnow().timestamp():
            raise HTTPException(status_code=403, detail="Token expired")
    except(jwt.PyJWTError, ValidationError):
        raise HTTPException(
            status_code=403, detail="Could not validate credentials")
