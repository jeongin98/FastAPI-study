# routes > users.py : 사용자 등록 및 로그인 처리를 위한 라우팅
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import select

from auth.hash_password import HashPassword
from auth.jwt_handler import create_access_token
from database.connection import get_session
from models.users import User, TokenResponse

user_router = APIRouter(
    tags=["User"],
)
users = {} ##
hash_password = HashPassword()

# 등록(/signup) 라우트
# 사용자를 등록하기 전 DB에 동일한 이메일이 존재하는지 확인
@user_router.post("/signup")
async def sign_user_up(user: User, session=Depends(get_session)) -> dict:
    statement = select(User).where(User.email == user.email)
    user_exist = session.exec(statement).first()

    if user_exist:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with supplied username exists"
        )
    
    hashed_password = hash_password.create_hash(user.password)
    user.password = hashed_password
    session.add(user)
    session.commit()

    return{
        "message": "User successfully registered!"
    }

# 로그인(/signin) 라우트
# 로그인하려는 사용자가 DB에 존재하는지 먼저 확인하고, 없으면 예외를 발생
# 사용자가 DB에 존재하면 패스워드가 일치하는지 확인해서 성공 또는 실패 메세지를 반환
@user_router.post("/signin", response_model=TokenResponse)
async def sign_user_in(user: OAuth2PasswordRequestForm = Depends(), session=Depends(get_session)) -> dict:
    statement = select(User).where(User.email == user.username)
    user_exist = session.exec(statement).first()
    if not user_exist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User with email does not exist"
        )
    
    if hash_password.verify_hash(user.password, user_exist.password):
        access_token = create_access_token(user_exist.email)
        return {
                "access_token" : access_token,
                "token_type" : "Bearer"
        }
    
    raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid details passed."
        )