from fastapi import FastAPI

from route.user import user


app = FastAPI()
app.include_router(user)


if __name__ == "__main__":
    pass
