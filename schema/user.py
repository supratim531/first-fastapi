def userEntity(user) -> dict:
    return {
        "_id": str(user["_id"]),
        "email": str(user["email"]),
        "username": str(user["username"]),
        "password": str(user["password"])
    }


def usersEntity(users) -> list:
    return [userEntity(user) for user in users]
