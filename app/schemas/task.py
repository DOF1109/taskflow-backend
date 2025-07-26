from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional
from app.models.task import TaskStatus, TaskPriority
from app.schemas.tag import Tag

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    status: TaskStatus = TaskStatus.PENDING
    priority: TaskPriority = TaskPriority.MEDIUM
    due_date: Optional[datetime] = None
    tags: List[str] = []

class TaskCreate(TaskBase):
    project_id: int

class TaskUpdate(TaskBase):
    pass

class TaskInDBBase(TaskBase):
    id: int
    owner_id: int
    tags: List[Tag] = []

    class Config:
        from_attributes = True

class Task(TaskInDBBase):
    pass 