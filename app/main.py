from fastapi import FastAPI
from pydantic import BaseModel
from app.tasks import add
from celery.result import AsyncResult
from app.worker import celery_app

app = FastAPI()

class TaskPayload(BaseModel):
    x: int
    y: int

@app.post("/tasks/")
def run_task(payload: TaskPayload):
    task = add.delay(payload.x, payload.y)
    return {"task_id": task.id}

@app.get("/tasks/{task_id}")
def get_status(task_id: str):
    result = AsyncResult(task_id, app=celery_app)
    return {"status": result.status, "result": result.result}