from fastapi import APIRouter

from domain.asset.factory import AssetFactory
from domain.user.repo import UserRepo
from domain.user.factory import UserFactory
from api.models import UserAdd, UserInfo, AssetInfo

user_router = APIRouter(prefix="/users")

repo = UserRepo("main_users.json")


@user_router.get("", response_model=list[UserInfo])
def get_all_users():
    return repo.get_all()


# TODO GET /users/{user_id}
@user_router.get("/{username}", response_model=UserInfo)
def get_user(username: str):
    return repo.get_by_username(username)


@user_router.post("", response_model=UserInfo)
def create_a_user(new_user: UserAdd):
    user = UserFactory().make_new(new_user.username)
    repo.add(user)
    return user


# TODO delete a user, DELETE /users/{user_id}


# TODO fix api, return asset info
@user_router.post("/{user_id}/assets", response_model=AssetInfo)
def add_asset_to_user(user_id: str, ticker: str):
    asset = AssetFactory().make_new(ticker)
    print(asset.__dict__)
    return asset
