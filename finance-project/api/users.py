from fastapi import APIRouter

from domain.asset.factory import AssetFactory
from domain.user.repo import UserRepo
from domain.user.factory import UserFactory
from api.models import UserAdd, UserInfo, AssetInfoUser
from persistence.user_file import UserPersistenceFile

users_router = APIRouter(prefix="/users")

user_persistence = UserPersistenceFile("main_users.json")
repo = UserRepo(user_persistence)


@users_router.get("", response_model=list[UserInfo])
def get_all_users():
    return repo.get_all()


# create POST /<user_id>/stocks
# the user can add a stock to its portfolio, by giving the ticker and the number of units it has
# save the country, full name of the company
# when we get a specific user we get the price of every stock the user has and the money it has on it


@users_router.get("/{username}", response_model=UserInfo)
def get_user(username: str):
    return repo.get_by_username(username)


@users_router.post("", response_model= UserInfo)
def create_a_user(new_user: UserAdd):
    user = UserFactory().make_new(new_user.username)
    repo.add(user)
    return user

# TODO delete a user, DELETE /users/{user_id}


@users_router.delete("/{user_id}", response_model=UserInfo)
def delete_a_user(username: str):
    pass

# TODO fix api, return asset info


@users_router.post("/{user_id}/assets", response_model=AssetInfoUser)
def add_asset_to_user(user_id: str, ticker: str):
    asset = AssetFactory().make_new(ticker)
    print(asset.__dict__)
    return asset
