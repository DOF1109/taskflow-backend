from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import crud, models
from app.api import deps
from app.models.task import TaskStatus

router = APIRouter()

@router.get("/", response_model=dict)
def get_dashboard_data(
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_user),
):
    total_tasks = len(crud.task.get_multi_by_owner(db, owner_id=current_user.id))
    completed_tasks = len(db.query(models.Task).filter(models.Task.owner_id == current_user.id, models.Task.status == TaskStatus.COMPLETED).all())
    pending_tasks = len(db.query(models.Task).filter(models.Task.owner_id == current_user.id, models.Task.status == TaskStatus.PENDING).all())
    in_progress_tasks = len(db.query(models.Task).filter(models.Task.owner_id == current_user.id, models.Task.status == TaskStatus.IN_PROGRESS).all())

    return {
        "total_tasks": total_tasks,
        "completed_tasks": completed_tasks,
        "pending_tasks": pending_tasks,
        "in_progress_tasks": in_progress_tasks,
    } 