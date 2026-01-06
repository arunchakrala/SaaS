from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.db.deps import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserRead

from app.core.security import hash_password

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", response_model=UserRead, status_code=status.HTTP_201_CREATED)
async def create_user(
    user_in: UserCreate,
    db: AsyncSession = Depends(get_db),
):
    # Check if email already exists
    result = await db.execute(
        select(User).where(User.email == user_in.email)
    )

    existing_user = result.scalar_one_or_none()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered.",
        )
    user = User(
        email = user_in.email,
        hashed_password = hash_password(user_in.password), #Temp
    )

    db.add(user)
    await db.commit()
    await db.refresh(user)

    return user