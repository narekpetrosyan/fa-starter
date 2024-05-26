from pydantic import BaseModel, ConfigDict


class UserBase(BaseModel):
    username: str


class UserCreate(BaseModel):
    pass


class UserRead(UserBase):
    model_config = ConfigDict(
        from_attributes=True,
    )
    id: int
