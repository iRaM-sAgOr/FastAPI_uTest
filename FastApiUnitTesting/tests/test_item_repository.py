import pytest
from schemas import ItemCreate
from repositories.item_repository import ItemRepository

@pytest.mark.asyncio
async def test_create_item(db_session):
    item_repo = ItemRepository(db_session)
    item_data = ItemCreate(name="mobile", description="a mobile phone")
    item = await item_repo.create_item(item_data)
    assert item.name == "mobile"
    assert item.description == "a mobile phone"
    assert item.id is not None