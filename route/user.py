from config.db import db

from fastapi import APIRouter

from model.user import User

from schema.user import userEntity, usersEntity


user = APIRouter()
collection = db.users


@user.get("/")
def root():
    status = "FastAPI Server is Running"
    return {
        "statusCode": 200,
        "status": status
    }


@user.get("/users")
def get_users():
    users = collection.find()
    return usersEntity(users)


@user.post("/create-user")
def create_user(user: User):
    print(user, type(user))
    insertedId = collection.insert_one(user.__dict__).inserted_id
    return {
        "statusCode": 200,
        "status": "User Inserted",
        "insertedId": str(insertedId)
    }


@user.get("/read-user/{username}")
def read_user(username: str):
    user = collection.find_one({"username": username})

    if user == None:
        return {
            "statusCode": 202,
            "status": f"Username {username} not found"
        }

    return userEntity(user)


@user.put("/update-user")
def update_user(username: str, user: User):
    updatedUser = collection.find_one_and_update(
        {"username": username},
        {"$set": user.__dict__},
        upsert=False
    )

    if updatedUser == None:
        return {
            "statusCode": 202,
            "status": f"Username {username} not found"
        }

    return {
        "statusCode": 200,
        "updatedUser": userEntity(collection.find_one({"username": user.username}))
    }


@user.delete("/delete-user")
def delete_user(username: str):
    deletedUser = collection.find_one_and_delete({"username": username})

    if deletedUser == None:
        return {
            "statusCode": 202,
            "status": f"Username {username} not found"
        }

    return {
        "statusCode": 200,
        "deletedUser": userEntity(deletedUser)
    }
