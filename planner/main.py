# main.py : 정의한 라우트를 등록하고 애플리케이션을 실행하는 파일    
# 서버 실행은 터미널에 다음 두 줄을 차례대로 입력
# > venv\Scripts\activate
# > python main.py 

# 라이브러리와 사용자 라우트 정의를 임포트
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from typing import List
from database.connection import conn

from routes.users import user_router
from routes.events import event_router

import uvicorn

app = FastAPI() # FastAPI 인스턴스 생성

# 라우트 등록
app. include_router(user_router, prefix="/user")
app. include_router(event_router, prefix="/event")

@app.on_event("startup")
def on_startup():
    conn()

@app.get("/")
async def home():
    return RedirectResponse(url="/event/")

if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)