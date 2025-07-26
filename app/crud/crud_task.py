from sqlalchemy.orm import Session
from typing import List, Union

from app.models.task import Task
from app.models.tag import Tag
from app.schemas.task import TaskCreate, TaskUpdate
from app.crud.crud_tag import tag as crud_tag

class CRUDTask:
    def get(self, db: Session, id: int) -> Union[Task, None]:
        return db.query(Task).filter(Task.id == id).first()

    def get_multi_by_owner(
        self, db: Session, *, owner_id: int, skip: int = 0, limit: int = 100
    ) -> list[Task]:
        return (
            db.query(Task)
            .filter(Task.owner_id == owner_id)
            .offset(skip)
            .limit(limit)
            .all()
        )

    def get_multi_by_project(
        self, db: Session, *, project_id: int, skip: int = 0, limit: int = 100
    ) -> list[Task]:
        return (
            db.query(Task)
            .filter(Task.project_id == project_id)
            .offset(skip)
            .limit(limit)
            .all()
        )
    
    def get_multi_by_owner_and_tags(
        self, db: Session, *, owner_id: int, tags: List[str], skip: int = 0, limit: int = 100
    ) -> list[Task]:
        return (
            db.query(Task)
            .filter(Task.owner_id == owner_id)
            .filter(Task.tags.any(Tag.name.in_(tags)))
            .offset(skip)
            .limit(limit)
            .all()
        )

    def create_with_owner(
        self, db: Session, *, obj_in: TaskCreate, owner_id: int
    ) -> Task:
        tags = crud_tag.get_or_create(db, tags=obj_in.tags)
        db_obj = Task(
            title=obj_in.title,
            description=obj_in.description,
            status=obj_in.status,
            priority=obj_in.priority,
            due_date=obj_in.due_date,
            owner_id=owner_id,
            project_id=obj_in.project_id,
            tags=tags
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: Task, obj_in: TaskUpdate
    ) -> Task:
        update_data = obj_in.dict(exclude_unset=True)
        if "tags" in update_data:
            tags = crud_tag.get_or_create(db, tags=update_data.pop("tags"))
            db_obj.tags = tags
        for field, value in update_data.items():
            setattr(db_obj, field, value)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def remove(self, db: Session, *, id: int) -> Union[Task, None]:
        obj = db.query(Task).get(id)
        db.delete(obj)
        db.commit()
        return obj

task = CRUDTask() 