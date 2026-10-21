from fastapi import FastAPI
from uuid import UUID   

app = FastAPI(
    title = "Student Management API"

)


student_data = {"id": 0, "name": "", "age": 0,"class":"", "reg no": ""}


@app.get("/")
def home():
    return {"message": "Welcome to the Student Management Centre!"}


@app.get("/student/{id}")  # Get a student by ID
def get_student_by_id(id: str):
    student = student_data.get(id)
    if not student:
        return {"error": "Student not found"}
    return student

@app.post("/student")  # Create a new student
def add_student(name: str, age: int, class_: str, reg_no: str):
    new_student = student_data.copy()
    new_student["id"] = str(UUID(int=len(student_data) + 1))
    new_student["name"] = name
    new_student["age"] = age
    new_student["class"] = class_
    new_student["reg no"] = reg_no

    student_data[new_student["id"]] = new_student
    return {"message": "Student added successfully", "data": new_student}

@app.put("/student/{id}")  # Update an existing student
def update_student(id: str, name: str, age: int, class_: str, reg_no: str):
    student = student_data.get(id)
    if not student:
        return {"error": "Student not found"}
    student["name"] = name
    student["age"] = age
    student["class"] = class_
    student["reg no"] = reg_no
    return {"message": "Student updated successfully", "data": student}

@app.delete("/student/{id}")  # Delete a student
def delete_student(id: str):
    student = student_data.get(id)
    if not student:
        return {"error": "Student not found"}
    del student_data[id]
    return {"message": "Student deleted successfully"}