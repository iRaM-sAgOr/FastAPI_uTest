import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
import pytest_asyncio
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from database import get_db
from models import Base
from typing import Any, Generator

from controllers.item_controller import router as item_router

def start_application():
    app = FastAPI()
    app.include_router(item_router, prefix="/api")
    return app

# Setup the in-memory SQLite database for testing
DATABASE_URL_ASYNC = "sqlite+aiosqlite:///:memory:"

# Asynchronous engine and session
async_engine = create_async_engine(
    DATABASE_URL_ASYNC,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
AsyncSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=async_engine, class_=AsyncSession
)

@pytest_asyncio.fixture(scope="function")
async def db_session() -> AsyncSession:
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    async with AsyncSessionLocal() as session:
        yield session
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

@pytest_asyncio.fixture(scope="function")
async def app() -> Generator[FastAPI, Any, None]:
    """
    Create a fresh database on each test case.
    """
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    _app = start_application()
    yield _app
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

@pytest_asyncio.fixture(scope="function")
async def client(
    app: FastAPI, db_session: AsyncSession
) -> Generator[TestClient, Any, None]:
    """
    Create a new FastAPI TestClient that uses the `db_session` fixture to override
    the `get_db` dependency that is injected into routes.
    """

    async def _get_test_db():
        try:
            yield db_session
        finally:
            pass

    app.dependency_overrides[get_db] = _get_test_db
    # Note: TestClient can only function in synchronous tests
    with TestClient(app) as client:
        yield client