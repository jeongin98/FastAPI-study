# models > users.py : 사용자 처리용 모델을 정의
from typing import Optional, List
from pydantic import BaseModel, EmailStr
from sqlmodel import SQLModel, Field
from models.events import Event

# 사용자 모델
class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None)
    email: EmailStr # 사용자 이메일 
    password: str # 사용자 패스워드

    # # 샘플 데이터 - 데이터 저장 및 설정할 때 참고 ##
    # class Config:
    #     schema_extra = {
    #         "example": {
    #             "email": "fastapi@packt.com",
    #             "password": "strong!!!",
    #             "events": [],
    #         }
    #     }

class TokenResponse(BaseModel): #JWT Response Model
    access_token: str
    token_type: str

# 사용자 로그인 모델
class UserSignIn(BaseModel):
    email: EmailStr
    password: str
 
    # class Config:
    #     schema_extra = {
    #         "example": {
    #             "email": "fastapi@packt.com",
    #             "password": "strong!!!",
    #             "events": [],
    #         }
    #     }