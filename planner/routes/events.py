# routes > events.py : 이벤트 생성, 변경, 삭제 등의 처리를 위한 라우팅
from fastapi import APIRouter, Depends, HTTPException, Request, status
from models.events import Event, EventUpdate # models.events 파일에 있는 Event 클래스를 가져오려 함 
from typing import List
from database.connection import get_session
from sqlmodel import select
from auth.authenticate import authenticate


event_router = APIRouter(
    tags=["Events"]
)

events = []

# 이벤트 추출
@event_router.get("/", response_model=List[Event])
async def retrieve_all_events(session=Depends(get_session)) -> List[Event]:
    statement = select(Event)
    events = session.exec(statement).all()
    return events

@event_router.get("/{id}", response_model=Event)
async def retrieve_event(id: int, session=Depends(get_session)) -> Event:
    event = session.get(Event, id)
    if event:
        return event
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event with supplied ID does not exist"
    )

# 이벤트 생성
@event_router.post("/new")
async def create_event(body: Event,session=Depends(get_session), user: str = Depends(authenticate)) -> dict:
    body.creator = user
    
    session.add(body)
    session.commit()
    session.refresh(body)

    return {
        "message": "Event created successfully"
    }

# 이벤트 삭제
@event_router.delete("/delete/{id}")
async def delete_event(id: int, session=Depends(get_session), user: str = Depends(authenticate)) -> dict:
    event = session.get(Event, id)
    if event:
        if event.creator != user:
            raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Operation not allowed"
                )
        session.delete(event)
        session.commit()
        return {
            "message": "Event deleted successfully"
        }
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event with supplied ID does not exist"
    )
  
@event_router.delete("/")
async def delete_all_events() -> dict:
    events.clear()
    return {
        "message": "Events deleted successfully"
    }

@event_router.put("/edit/{id}", response_model=Event)
async def update_event(id: int, new_data: EventUpdate, session=Depends(get_session)) -> Event:
    event = session.get(Event, id)
    if event:
        event_data = new_data.dict(exclude_unset=True)
        for key, value in event_data.items():
            setattr(event, key, value)
        session.add(event)
        session.commit()
        session.refresh(event)

        return event
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event with supplied ID does not exist"
    )