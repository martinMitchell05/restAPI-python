from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    email: str

users_db = []

# Get all users
@app.get("/users", response_model=List[User])
def get_users():
    return users_db

# Get user by id
@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
    for user in users_db:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

# Create new user
@app.post("/users", response_model=User)
def create_user(user: User):
    users_db.append(user)
    return user

# Update user
@app.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, updated_user: User):
    for i, user in enumerate(users_db):
        if user.id == user_id:
            users_db[i] = updated_user
            return updated_user
    raise HTTPException(status_code=404, detail="User not found")

# Delete user
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    for i, user in enumerate(users_db):
        if user.id == user_id:
            users_db.pop(i)
            return {"message": "User deleted"}
    raise HTTPException(status_code=404, detail="User not found")


# Execute API: `uvicorn file:app --reload`
# Search for http://127.0.0.1:8000/docs and check
