from fastapi import APIRouter
from api.users import users_router

users_router = APIRouter(prefix="/users")


@users_router.get()
def get_all_users():
    return []


@users_router.post("/")
def create_a_user():
    pass
