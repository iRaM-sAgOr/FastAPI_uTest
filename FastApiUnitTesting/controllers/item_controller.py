# controllers/item_controller.py
from fastapi import APIRouter, Depends
from services.item_service import ItemService
from repositories.item_repository import ItemRepository
from schemas import ItemCreate, ItemResponse
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db

router = APIRouter()

@router.post("/items", response_model=ItemResponse)
async def create_item(item: ItemCreate, db: AsyncSession = Depends(get_db)):
    item_repository = ItemRepository(db)
    item_service = ItemService(item_repository)
    return await item_service.create_item(item)

@router.get("/items/{item_id}", response_model=ItemResponse)
async def get_item(item_id: int, db: AsyncSession = Depends(get_db)):
    item_repository = ItemRepository(db)
    item_service = ItemService(item_repository)
    return await item_service.get_item(item_id)