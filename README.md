# FASTAPI-ORMAR-UTILITIES
![](https://www.code-inspector.com/project/19657/score/svg)
## Small package for better interaction with Ormar ORM.

### This package makes your views cleaner

### Features:
* Fully async
* Compatible with FastAPI
* In my opinion Ormar is the best ORM for FastAPI


### Example usage:
```python

from fastapi import APIRouter, Depends
from fastapi_ormar_utilities import Base

from .models import Item # import Ormar model
from .schemas import ItemCreate # import Pydantic model

router = APIRouter()

class ItemService(Base):
    model = Item

@router.get('/')
async def get_items(
    service: ItemService = Depends()
):
    return await service.fetch_all()

@router.post('/')
async def create_item(
    item_data: ItemCreate,
    service: ItemService = Depends()
):
    return await service.create(item_data)
```
