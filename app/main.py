from fastapi import FastAPI
from app.tasks import add

app = FastAPI()

@app.post("/add")
def queue_add(x: int, y: int):
    task = add.delay(x, y)
    return {"task_id": task.id}

@app.get("/result/{task_id}")
def get_result(task_id: str):
    result = add.AsyncResult(task_id)
    return {
        "task_id": task_id,
        "status": result.status,
        "result": result.result
    }
