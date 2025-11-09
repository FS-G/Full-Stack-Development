# core/db.py
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
# from core.settings import settings

DATABASE_URL="postgresql+asyncpg://postgres:UEOtcIxovPWqdbzfjXTtfhFQxENZJXLk@maglev.proxy.rlwy.net:32491/railway"
JWT_SECRET="supersecret"

engine = create_async_engine(DATABASE_URL, pool_pre_ping=True)
AsyncSessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
Base = declarative_base()

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session