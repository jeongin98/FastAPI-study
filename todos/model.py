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

#UPDATE 라우트의 요청 바디용 모델
class TodoItem(BaseModel):
    item: str

    class Config:
        schema_extra = {
            "example:" : {
                "item" : "Read the next chapter of the book"
            }
        }
