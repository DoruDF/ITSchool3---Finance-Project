from pydantic import BaseModel, Field
from uuid import UUID


class UserAdd(BaseModel):
    username: str = Field(description="Alphanumeric username between 6 and 20 chars")


class UserInfo(BaseModel):
    id: UUID
    username: str
    stocks: list[str]

    class Config:
        orm_mode = True


class AssetInfoBase(BaseModel):
    ticker: str
    name: str
    country: str
    # TODO refactor to not have duplicate code

    class Config:
        orm_mode = True


class AssetInfoUser(AssetInfoBase):
    units: float


class AssetInfoPrice(AssetInfoBase):
    current_price: float
    currency: str
    today_low_price: float
    today_high_price: float
    open_price: float
    close_price: float
    fifty_day_price: float
    up_or_down_percentage: float
