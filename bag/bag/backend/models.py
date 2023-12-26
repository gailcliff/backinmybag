from pydantic import BaseModel, EmailStr, Field
from .bag.back_in import models as db_models

from typing import Optional, Type


class CustomModel(BaseModel):
    id: Optional[int] = None
    __schema_cls__: Type[db_models.DbModel]

    def save(self):
        db_model = self.__schema_cls__.__call__(**self.model_dump())

        db_model.save()

        self.id = db_model.id

        print(f"saved a record with id: {self.id}")

    @classmethod
    def fetch_all(cls):
        return list(cls.__schema_cls__.objects.all().values())


class User(CustomModel):
    user_name: str
    phone: str
    email: EmailStr
    __schema_cls__ = db_models.User

