from app.models.user import User

user = User(
    email="test@example.com",
    hashed_password = "asdasd8eyr87eufb@",
)

print(user.email)
print(user.is_active)
print(user.is_verified)
print(user.is_superuser)
print(user.created_at)