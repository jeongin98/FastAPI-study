from fastapi import APIRouter

todo_router = APIRouter() # FastAPI instance

todo_list = [] # 앱 내부 데이터베이스를 임시로 만듦

# todo 생성 및 추출하는 라우터 정의

# todo_list에 todo를 추가하는 POST 메서드
@todo_router.post("/todo")
async def add_todo(todo: dict) -> dict:
    todo_list.append(todo)
    return {
        "message" : "Todo added successfully."
    }

# todo_list 에서 모든 todo를 조회하는 GET 메서드
@todo_router.get("/todo")
async def retrieve_todos() -> dict:
    return {
        "todos" : todo_list
    }

# APIRouter 클래스를 사용해 정의한 라우트를 FastAPI() 인스턴스에 추가해야 외부에서 접근 가능
# todo 라우트를 외부로 공개하기 위해 include_router() 메서드 사용 => todo_router를 FastAPI() 인스턴스에 추가
