from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.users import router as users_router

from app.db.deps import get_db

app = FastAPI(title="SaaS Backend")

app.include_router(users_router)


@app.get("/health")
async def health_check(db: AsyncSession = Depends(get_db)):
    return {"status": "ok"}
