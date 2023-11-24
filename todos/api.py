from fastapi import FastAPI
from todo import todo_router

app = FastAPI() # FastAPI instance

@app.get("/")
async def welcome() -> dict:
    return {
        "message" : "Hello World"
    }

# APIRouter 클래스를 사용해 정의한 라우트를 FastAPI() 인스턴스에 추가해야 외부에서 접근 가능
# todo 라우트를 외부로 공개하기 위해 include_router() 메서드 사용 => todo_router를 FastAPI() 인스턴스에 추가
app.include_router(todo_router)
