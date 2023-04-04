from pydantic import BaseModel, Field
from uuid import UUID


class UserAdd(BaseModel):
    username: str = Field(
        description="Alphanumeric username between 6 and 20 characters."
    )


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
    sector: str

    class Config:
        orm_mode = True

class AssetInfoUser(AssetInfoBase):
    units: float

class AssetInfoPrice(AssetInfoBase):
    currency: str
    current_price: float
    # TODO homework
    today_low_price: float
    today_high_price: float
    open_price: float
    closed_price: float
    fifty_day_price: float
    price_evolution: str
