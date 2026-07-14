from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(title="To-Do List REST API")

# -----------------------------
# Models
# -----------------------------

class TodoCreate(BaseModel):
    title: str


class TodoUpdate(BaseModel):
    title: str
    completed: bool


class Todo(BaseModel):
    id: int
    title: str
    completed: bool


# -----------------------------
# In-memory Storage
# -----------------------------

todos = []
next_id = 1


# -----------------------------
# Home
# -----------------------------

@app.get("/")
def home():
    return {
        "message": "Welcome to To-Do REST API",
        "swagger": "http://127.0.0.1:8000/docs"
    }


# -----------------------------
# Create Task
# POST /todos
# -----------------------------

@app.post("/todos", response_model=Todo, status_code=201)
def create_todo(todo: TodoCreate):
    global next_id

    new_todo = {
        "id": next_id,
        "title": todo.title,
        "completed": False
    }

    todos.append(new_todo)
    next_id += 1

    return new_todo


# -----------------------------
# Get All Tasks
# GET /todos
# -----------------------------

@app.get("/todos", response_model=List[Todo])
def get_all_todos():
    return todos


# -----------------------------
# Get One Task
# GET /todos/{id}
# -----------------------------

@app.get("/todos/{id}", response_model=Todo)
def get_todo(id: int):

    for todo in todos:
        if todo["id"] == id:
            return todo

    raise HTTPException(status_code=404, detail="Task not found")


# -----------------------------
# Update Task
# PUT /todos/{id}
# -----------------------------

@app.put("/todos/{id}", response_model=Todo)
def update_todo(id: int, updated: TodoUpdate):

    for todo in todos:

        if todo["id"] == id:

            todo["title"] = updated.title
            todo["completed"] = updated.completed

            return todo

    raise HTTPException(status_code=404, detail="Task not found")


# -----------------------------
# Delete Task
# DELETE /todos/{id}
# -----------------------------

@app.delete("/todos/{id}")
def delete_todo(id: int):

    for todo in todos:

        if todo["id"] == id:

            todos.remove(todo)

            return {
                "message": "Task deleted successfully"
            }

    raise HTTPException(status_code=404, detail="Task not found")