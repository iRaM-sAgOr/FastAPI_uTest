# services/item_service.py
from repositories.item_repository import ItemRepository
from schemas import ItemCreate, ItemResponse

class ItemService:
    def __init__(self, item_repository: ItemRepository):
        self.item_repository = item_repository

    async def create_item(self, item: ItemCreate) -> ItemResponse:
        db_item = await self.item_repository.create_item(item)
        return ItemResponse(id=db_item.id, name=db_item.name, description=db_item.description)

    async def get_item(self, item_id: int) -> ItemResponse:
        db_item = await self.item_repository.get_item(item_id)
        return ItemResponse(id=db_item.id, name=db_item.name, description=db_item.description)