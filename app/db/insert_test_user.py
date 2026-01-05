import asyncio

from app.db.session import AsyncSessionLocal
from app.models.user import User

async def main():
    async with AsyncSessionLocal() as session:
        user = User(
            email="first@example.com",
            hashed_password = "fake_hash"
        )

        session.add(user)

        await session.commit()
        await session.refresh(user)

        print("id:", user.id)
        print("is_active:", user.is_active)
        print("is_verified:", user.is_verified)
        print("is_superuser:", user.is_superuser)
        print("created_at:", user.created_at)
        print("updated_at:", user.updated_at)

asyncio.run(main())