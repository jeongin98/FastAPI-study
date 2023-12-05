# models > events.py : 이벤트 처리용 모델을 정의
from sqlmodel import JSON, SQLModel, Field, Column
from typing import Optional, List

class Event(SQLModel, table=True):
    id : int  = Field(default=None, primary_key=True) # 자동 생성되는 고유 식별자
    title : str # 이벤트 타이틀
    image : str # 이벤트 이미지 배너의 링크
    description : str # 이벤트 설명
    tags : List[str] = Field(sa_column=Column(JSON))# 그룹화를 위한 이벤트 태그
    location : str # 이벤트 위치

    # 샘플 데이터 - API를 통해 신규 이벤트를 생성할 때 참고
    class Config:
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "title": "FastAPI Book Launch",
                "image": "https://linktomyimage.com/image.png",
                "description": "We will be discussing the contents of the FastAPI book in this event.Ensure to come with your own copy to win gifts!",
                "tags": ["python", "fastapi", "book", "launch"],
                "location": "Google Meet"
            }
        }

class EventUpdate(SQLModel):
    title: Optional[str]
    image: Optional[str]
    description: Optional[str]
    tags: Optional[List[str]]

    class Config:
        schema_extra = {
            "example": {
                "title": "FastAPI Book Launch",
                "image": "https://linktomyimage.com/image.png",
                "description": "We will be discussing the contents of the FastAPI book in this event.Ensure to come with your own copy to win gifts!",
                "tags": ["python", "fastapi", "book", "launch"],
                "location": "Google Meet"
            }
        }