# main.py : 정의한 라우트를 등록하고 애플리케이션을 실행하는 파일    
# 실행은 터미널에 python main.py 입력

# 라이브러리와 사용자 라우트 정의를 임포트
from fastapi import FastAPI
from routes.users import user_router

import uvicorn

app = FastAPI() # FastAPI 인스턴스 생성

# 라우트 등록
app. include_router(user_router, prefix="/user")


if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)