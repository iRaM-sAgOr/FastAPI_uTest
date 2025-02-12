from sqlalchemy.ext.asyncio import AsyncSession
from schemas import ItemCreate
from models import Item

class ItemRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_item(self, item: ItemCreate) -> Item:
        db_item = Item(name=item.name, description=item.description)
        self.db.add(db_item)
        await self.db.commit()
        await self.db.refresh(db_item)
        return db_item

    async def get_item(self, item_id: int) -> Item:
        return await self.db.get(Item, item_id)