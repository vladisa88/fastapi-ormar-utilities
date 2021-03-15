import typing as tp

import ormar
from pydantic import BaseModel

from fastapi_ormar_utilities.decorators import handle_exception


class Base:
    """
    Base class for interaction with
    Ormar ORM
    """
    model: ormar.Model

    async def fetch_all(self, related_field: str = None) -> tp.List[ormar.Model]:
        """
        Fetch all objects from db

        :param related_field: Name of the field to perform
        `select_related` method
        """
        if related_field:
            return await self.model.objects.select_related(related_field).all()
        return await self.model.objects.all()

    async def create(self, schema: BaseModel, **kwargs: tp.Any) -> ormar.Model:
        """
        Create a new object
        """
        obj = await self.model.objects.create(
            **schema.dict(exclude_unset=True), **kwargs
        )
        return obj

    @handle_exception
    async def fetch_one(self, unique_id: int, related_field: str = None) -> ormar.Model:
        """
        Fetch one object using pk

        :param unique_id: Primary key in database
        :param related_field: Name of the field to perform
        `select_related` method
        """
        if related_field:
            return await self.model.objects.select_related(related_field).get(pk=unique_id)
        return await self.model.objects.get(pk=unique_id)

    @handle_exception
    async def fetch_one_by_param(self, related_field: str = None, **kwargs) -> ormar.Model:
        """
        Fetch one object using any params

        :param related_field: Name of the field to perform
        `select_related` method
        """
        if related_field:
            return await self.model.objects.select_related(related_field).get(**kwargs)
        return await self.model.objects.get(**kwargs)

    async def filter(self, related_field: str = None, **kwargs) -> ormar.Model:
        """
        Fetch objects using special params

        :param related_field: Name of the field to perform
        `select_related` method
        """
        if related_field:
            await self.model.objects.select_related(related_field).all(**kwargs)
        return await self.model.objects.all(**kwargs)

    async def update(self, unique_id: int, schema: BaseModel) -> ormar.Model:
        """
        Update one object in database
        """
        obj = await self.fetch_one(unique_id)
        return await obj.update(schema.dict(exclude_unset=True))

    async def delete(self, unique_id: int) -> None:
        """
        Remove object from database
        """
        obj = await self.fetch_one(unique_id)
        await obj.delete()
