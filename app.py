from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# ---------------------------------------------------------------------------
# Model
# ---------------------------------------------------------------------------

class Student(BaseModel):
    name: str
    age: int
    course: str


# ---------------------------------------------------------------------------
# In-memory storage
# ---------------------------------------------------------------------------

students = {}


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------

@app.post("/students/{student_id}")
def add_student(student_id: int, student: Student):
    if student_id in students:
        return {"error": "Student already exists"}
    students[student_id] = student
    return {"message": "Student added", "data": student}


@app.get("/students/{student_id}")
def get_student(student_id: int):
    if student_id not in students:
        return {"error": "Student not found"}
    return students[student_id]


@app.get("/students")
def list_students():
    return students


@app.put("/students/{student_id}")
def update_student(student_id: int, student: Student):
    if student_id not in students:
        return {"error": "Student not found"}
    students[student_id] = student
    return {"message": "Student updated", "data": student}


@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"error": "Student not found"}
    del students[student_id]
    return {"message": "Student deleted"}


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
