Title: Day 2 – FastAPI CRUD with In-Memory Storage
Date: 2026-04-16
Category: GenAI
Tags: Python, FastAPI, CRUD, POST, GET, DELETE, Beginner
Slug: day2-fastapi-crud-in-memory
Status: published

On Day 1 we understood GET and POST. On Day 2, we build a simple CRUD API — Create, Read, Update, Delete — using an in-memory dictionary. No database yet, just pure FastAPI.

## What is CRUD?

| Operation | HTTP Method | What it does          |
|-----------|-------------|----------------------|
| Create    | POST        | Add new data         |
| Read      | GET         | Fetch existing data  |
| Update    | PUT         | Modify existing data |
| Delete    | DELETE      | Remove data          |

## The Student API

We'll build an API to manage student records — add, fetch, update, and delete.

## Pydantic Model

```python
from pydantic import BaseModel

class Student(BaseModel):
    name: str
    age: int
    course: str
```

## In-Memory Storage

```python
students = {}  # acts as our temporary database
```

## POST – Add a Student

```python
@app.post("/students/{student_id}")
def add_student(student_id: int, student: Student):
    if student_id in students:
        return {"error": "Student already exists"}
    students[student_id] = student
    return {"message": "Student added", "data": student}
```

## GET – Fetch a Student

```python
@app.get("/students/{student_id}")
def get_student(student_id: int):
    if student_id not in students:
        return {"error": "Student not found"}
    return students[student_id]
```

## GET – List All Students

```python
@app.get("/students")
def list_students():
    return students
```

## PUT – Update a Student

```python
@app.put("/students/{student_id}")
def update_student(student_id: int, student: Student):
    if student_id not in students:
        return {"error": "Student not found"}
    students[student_id] = student
    return {"message": "Student updated", "data": student}
```

## DELETE – Remove a Student

```python
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"error": "Student not found"}
    del students[student_id]
    return {"message": "Student deleted"}
```

## Test it on Swagger UI

Run the app and open:

```
http://127.0.0.1:8000/docs
```

Try each endpoint in order — POST first, then GET, PUT, DELETE.

> In-memory storage resets every time you restart the server. Day 3 will connect this to a real database.
