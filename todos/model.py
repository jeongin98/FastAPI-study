from typing import List

from pydantic import BaseModel


# 두 개의 필드만 허용하는 pydantic 모델 생성
class Todo(BaseModel):
    id: int
    item: str

    class Config: # 샘플 데이터 정의 => 모델 클래스 안에 Config 클래스로 정의
        schema_extra = {
            "example": {
                "id": 1,
                "item": "Example Schema!"
            }
        }

# UPDATE 라우트의 요청 바디용 모델
class TodoItem(BaseModel):
    item: str

    class Config:
        schema_extra = {
            "example:" : {
                "item" : "Read the next chapter of the book"
            }
        }

# 모든 todo를 추출해서 배열로 반환하는 라우트
# ID 없이 todo 아이템만 반환하도록 변경
class TodoItems(BaseModel):
    todos: List[TodoItem]

    class Config:
        schema_extra = {
            "example": {
                "todos": [
                    {
                        "item": "Example schema 1!"
                    },
                    {
                        "item": "Example schema 2!"
                    }
                ]
            }
        }