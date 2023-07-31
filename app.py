from fastapi import FastAPI
from pydantic import BaseModel
from typing import Any
from celery.result import AsyncResult
from tasks import generate_task


app = FastAPI()


class Item(BaseModel):
    prompt: str


@app.post("/generate/")
async def generate_text(item: Item) -> Any:
    task = generate_task.delay(item.prompt)
    task_id = task.id
    return {"task_id": task_id}


@app.get("/task/{task_id}")
async def get_task(task_id: str) -> Any:    
    result = AsyncResult(task_id)
    if result.ready():
        res = result.get()
        return {            
            "time": res[0],
            "result": res[1],
            # "memory": res[2],
            "status": "Task completed",
        }
    else:
        return {"status": "Task not completed yet"}
