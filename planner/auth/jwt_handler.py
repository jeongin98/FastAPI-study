import time
from typing import Optional
from pydantic import BaseSettings
from datetime import datetime
from database.connection import Settings
from fastapi import HTTPException, status
from jose import jwt, JWTError


class Settings(BaseSettings):
    SECRET_KEY: Optional[str] = None
    class Config:
        env_file = ".env"

settings = Settings()

def create_access_token(user: str):
    payload = {
        "user" : user,
        "expires" : time.time() + 3600
    }

    token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")

    return token

def verify_access_token(token: str):
    try:
        data = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])

        expire = data.get("expires")
        if expire is None:
            raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="No access token supplied")

        if datetime.utcnow() > datetime.utcfromtimestamp(expire):
            raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="No access token supplied")
        
        return data
    
    except JWTError:
         raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid token")
        

