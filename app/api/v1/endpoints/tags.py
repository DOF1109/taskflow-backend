from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app import schemas, models, crud
from app.api import deps

router = APIRouter()

@router.get("/", response_model=List[schemas.Tag])
def read_tags(skip: int = 0, limit: int = 100, db: Session = Depends(deps.get_db)):
    return crud.tag.get_multi(db, skip=skip, limit=limit)

@router.post("/", response_model=schemas.Tag)
def create_tag(tag_in: schemas.TagCreate, db: Session = Depends(deps.get_db)):
    db_tag = crud.tag.get_by_name(db, name=tag_in.name)
    if db_tag:
        raise HTTPException(status_code=400, detail="Tag already exists")
    return crud.tag.create(db, obj_in=tag_in)

@router.get("/{tag_id}", response_model=schemas.Tag)
def read_tag(tag_id: int, db: Session = Depends(deps.get_db)):
    tag = crud.tag.get(db, id=tag_id)
    if not tag:
        raise HTTPException(status_code=404, detail="Tag not found")
    return tag

@router.put("/{tag_id}", response_model=schemas.Tag)
def update_tag(tag_id: int, tag_in: schemas.TagUpdate, db: Session = Depends(deps.get_db)):
    tag = crud.tag.get(db, id=tag_id)
    if not tag:
        raise HTTPException(status_code=404, detail="Tag not found")
    return crud.tag.update(db, db_obj=tag, obj_in=tag_in)

@router.delete("/{tag_id}", response_model=schemas.Tag)
def delete_tag(tag_id: int, db: Session = Depends(deps.get_db)):
    tag = crud.tag.get(db, id=tag_id)
    if not tag:
        raise HTTPException(status_code=404, detail="Tag not found")
    return crud.tag.remove(db, id=tag_id)
