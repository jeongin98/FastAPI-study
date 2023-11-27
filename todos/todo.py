from fastapi import APIRouter, Path
from todos.model import Todo, TodoItem, TodoItems

todo_router = APIRouter() # FastAPI instance

todo_list = [] # 앱 내부 데이터베이스를 임시로 만듦

# todo 생성 및 추출하는 라우터 정의

# todo_list에 todo를 추가하는 POST 메서드
@todo_router.post("/todo")
async def add_todo(todo: Todo) -> dict: # 타입 어노테이션을 (todo: Todo)로 명시함으로써 요청 데이터 타입을 Todo로 제한
    todo_list.append(todo)
    return {
        "message" : "Todo added successfully."
    }

# todo_list 에서 모든 todo를 조회하는(가져오는) GET 메서드
@todo_router.get("/todo", response_model=TodoItems)
async def retrieve_todos() -> dict:
    return {
        "todos" : todo_list
    }

@todo_router.get("/todo/{todo_id}")
async def get_single_todo(todo_id: int = Path(..., title="The ID of the todo to retrieve.")) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            return {"todo": todo}
    
    return {"message": "Todo with supplied ID doesn't exist."}

# todo 변경 라우트
@todo_router.put("/todo/{todo_id}")
async def update_todo(todo_data: TodoItem, todo_id: int = Path(..., title="The ID of the todo to be updated.")) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            todo.item = todo_data.item
            return{
                "message" : "Todo updated successfully."
            }
    return {
        "message" : "Todo with suppied ID doesn't exist."
    }

# 삭제를 위한 라우트
@todo_router.delete("/todo/{todo_id}")
async def delete_single_todo(todo_id: int) -> dict:
  for index in range(len(todo_list)):
      todo = todo_list[index]
      if todo.id == todo_id:
          todo_list.pop(index)
          return {
              "message": "Todo deleted successfully."
          }
  return {
      "message": "Todo with supplied ID doesn't exist."
  }

@todo_router.delete("/todo")
async def delete_all_todo() -> dict:
  todo_list.clear()
  return {
      "message": "Todos deleted successfully."
  }