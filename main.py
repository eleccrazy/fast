from typing import Dict, List

from fastapi import FastAPI

app = FastAPI()

items = []


@app.get("/")
def root() -> Dict[str, str]:
    return {"message": "Hello, there"}


@app.post("/tasks")
def add_tasks(item: str) -> List[str]:
    items.append(item)
    return items


@app.get("/tasks/{task_id}")
def get_task_by_id(task_id: int) -> Dict[str, str] | str:
    if task_id >= len(items):
        return {"Message": f"An item with id {task_id} not found"}
    return items[task_id]
