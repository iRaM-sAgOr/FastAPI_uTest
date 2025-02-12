from fastapi import FastAPI
from database import engine
from controllers.item_controller import router as item_router
from contextlib import asynccontextmanager
from models import Base

# Create database tables (for demonstration purposes)
@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)
# Include the router
app.include_router(item_router, prefix="/api")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)
