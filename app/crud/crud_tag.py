from sqlalchemy.orm import Session
from typing import List, Union

from app.models.tag import Tag
from app.schemas.tag import TagCreate

class CRUDTag:
    def get(self, db: Session, id: int) -> Union[Tag, None]:
        return db.query(Tag).filter(Tag.id == id).first()

    def get_multi(self, db: Session, skip: int = 0, limit: int = 100) -> list[Tag]:
        return db.query(Tag).offset(skip).limit(limit).all()
    def get_by_name(self, db: Session, *, name: str) -> Union[Tag, None]:
        return db.query(Tag).filter(Tag.name == name).first()

    def create(self, db: Session, *, obj_in: TagCreate) -> Tag:
        db_obj = Tag(name=obj_in.name)
        db.add(db_obj)
        try:
            db.commit()
        except Exception as e:
            db.rollback()
            # Opcional: puedes importar IntegrityError de sqlalchemy.exc y filtrar por ese tipo
            raise ValueError("Tag with this name already exists or DB error: " + str(e))
        db.refresh(db_obj)
        return db_obj

    def get_or_create(self, db: Session, *, tags: List[str]) -> List[Tag]:
        tag_objects = []
        for tag_name in tags:
            tag = self.get_by_name(db, name=tag_name)
            if not tag:
                tag = self.create(db, obj_in=TagCreate(name=tag_name))
            tag_objects.append(tag)
        return tag_objects

tag = CRUDTag() 