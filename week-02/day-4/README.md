# 📝 To-Do List REST API (FastAPI)

A simple To-Do List REST API built using **FastAPI**. This project allows users to create, retrieve, update, and delete tasks. All data is stored in an in-memory Python list without using a database, as required by the lab instructions. :contentReference[oaicite:0]{index=0}

---

## 📌 Features

- Add a new task
- View all tasks
- View a task by ID
- Update an existing task
- Delete a task
- Automatic API documentation using Swagger UI
- No database required (uses Python list)

---

## 🛠️ Technologies Used

- Python 3.x
- FastAPI
- Uvicorn
- Pydantic

---

## 📂 Project Structure

```
Todo-REST-API/
│
├── main.py
├── README.md
└── screenshots/
    ├── create.png
    ├── get_all.png
    ├── get_by_id.png
    ├── update.png
    ├── delete.png
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/todo-rest-api.git
cd todo-rest-api
```

### 2. Install Dependencies

```bash
pip install fastapi uvicorn
```

### 3. Run the Application

```bash
uvicorn main:app --reload
```

The server will start at:

```
http://127.0.0.1:8000
```

The application is configured as a FastAPI project with automatic Swagger documentation. :contentReference[oaicite:1]{index=1}

---

## 📖 API Documentation

### Swagger UI

```
http://127.0.0.1:8000/docs
```

### ReDoc

```
http://127.0.0.1:8000/redoc
```

---

# API Endpoints

## 1. Home

**GET /**

Returns a welcome message.

### Response

```json
{
  "message": "Welcome to To-Do REST API",
  "swagger": "http://127.0.0.1:8000/docs"
}
```

---

## 2. Create Task

**POST /todos**

### Request Body

```json
{
  "title": "Finish Python Assignment"
}
```

### Response

```json
{
  "id": 1,
  "title": "Finish Python Assignment",
  "completed": false
}
```

Implemented as the task creation endpoint using an auto-incrementing ID and default `completed` value of `false`. :contentReference[oaicite:2]{index=2}

---

## 3. Get All Tasks

**GET /todos**

### Response

```json
[
  {
    "id": 1,
    "title": "Finish Python Assignment",
    "completed": false
  }
]
```

Returns all stored tasks. :contentReference[oaicite:3]{index=3}

---

## 4. Get Task by ID

**GET /todos/{id}**

### Example

```
GET /todos/1
```

### Success Response

```json
{
  "id": 1,
  "title": "Finish Python Assignment",
  "completed": false
}
```

### Error Response

```json
{
  "detail": "Task not found"
}
```

Returns a specific task or a 404 error if it does not exist. :contentReference[oaicite:4]{index=4}

---

## 5. Update Task

**PUT /todos/{id}**

### Request Body

```json
{
  "title": "Complete FastAPI Lab",
  "completed": true
}
```

### Response

```json
{
  "id": 1,
  "title": "Complete FastAPI Lab",
  "completed": true
}
```

Allows updating both the task title and completion status. :contentReference[oaicite:5]{index=5}

---

## 6. Delete Task

**DELETE /todos/{id}**

### Response

```json
{
  "message": "Task deleted successfully"
}
```

Deletes the specified task and returns a success message. :contentReference[oaicite:6]{index=6}

---

# 🧪 Testing

The API can be tested using:

- Swagger UI
- Postman

The lab instructions specifically require testing all APIs using both Postman and Swagger UI and submitting screenshots of API responses. :contentReference[oaicite:7]{index=7}

---

# 📋 Lab Requirements Completed

- ✅ FastAPI Used
- ✅ No Database
- ✅ Data Stored in Python List
- ✅ POST Endpoint
- ✅ GET All Endpoint
- ✅ GET by ID Endpoint
- ✅ PUT Endpoint
- ✅ DELETE Endpoint
- ✅ Swagger Documentation
- ✅ Ready for Postman Testing
