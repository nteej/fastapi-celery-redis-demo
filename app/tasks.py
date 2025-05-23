from app.worker import celery_app

@celery_app.task(name="add_task")
def add(x: int, y: int):
    return x + y