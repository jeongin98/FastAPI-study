# models > users.py : 사용자 처리용 모델을 정의
from pydantic import BaseModel, EmailStr
from typing import Optional, List
from models.events import Event

# 사용자 모델
class User(BaseModel):
    email: EmailStr # 사용자 이메일
    password: str # 사용자 패스워드
    events: Optional[List[Event]] # 해당 사용자가 생성한 이벤트, 처음에는 비어 있다.

    # 샘플 데이터 - 데이터 저장 및 설정할 때 참고
    class Config:
        schema_extra = {
            "example": {
                "email": "fastapi@packt.com",
                "username": "strong!!!",
                "events": [],
            }
        }

# 사용자 로그인 모델
class UserSignIn(BaseModel):
    email: EmailStr
    password: str
 
    class Config:
        schema_extra = {
            "example": {
                "email": "fastapi@packt.com",
                "password": "strong!!!",
                "events": [],
            }
        }