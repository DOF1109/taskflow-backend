from fastapi import APIRouter

from app.api.v1.endpoints import login, projects, tasks, dashboard, tags

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(projects.router, prefix="/projects", tags=["projects"])
api_router.include_router(tasks.router, prefix="/tasks", tags=["tasks"])
api_router.include_router(dashboard.router, prefix="/dashboard", tags=["dashboard"])

api_router.include_router(tags.router, prefix="/tags", tags=["tags"])
