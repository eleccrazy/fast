from typing import Dict, List

from fastapi import FastAPI, HTTPException, status

app = FastAPI()

items = []


@app.get("/")
def root() -> Dict[str, str]:
    return {"message": "Hello, there"}


@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def add_tasks(item: str) -> List[str]:
    items.append(item)
    return items


@app.get("/tasks/{task_id}")
def get_task_by_id(task_id: int) -> Dict[str, str] | str:
    if task_id >= len(items):
        raise HTTPException(
            status_code=404, detail=f"An item with id {task_id} not found"
        )
    return items[task_id]


@app.get("/tasks")
def get_all_tasks() -> List[str]:
    return items
