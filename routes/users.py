from fastapi import APIRouter, HTTPException, status, Depends
from database.connection import get_session
from database.users import *
from models.users import User, TokenResponse
from auth.hash_password import HashPassword
from fastapi.security import OAuth2PasswordRequestForm
from auth.jwt_handler import create_access_token
from auth.authenticate import authenticate

user_router = APIRouter(
    tags=["User"],
)


hash_password = HashPassword()


@user_router.post("/signup")
async def sign_user_up(new_user: User) -> dict:

    if get_user(new_user.email) is not None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with supplied username exists"
        )

    hashed_password = hash_password.create_hash(new_user.password)
    new_user.password = hashed_password

    add_user(new_user)

    return {
        "message": "User successfully registered!"
    }


@user_router.post("/signin", response_model=TokenResponse)
async def sign_user_in(auth: OAuth2PasswordRequestForm = Depends()) -> dict:

    user_exist = get_user(auth.username)

    if user_exist is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User does not exist"
        )

    if hash_password.verify_hash(auth.password, user_exist.password):
        access_token = create_access_token(user_exist.email)

    return {
        "access_token": access_token,
        "token_type": "Bearer"
    }


@user_router.get("/balance")
async def retrieve_transactions(email: str = Depends(authenticate)) -> dict:

    user = get_user(email)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User does not exist"
        )

    return { "balance": user.balance }
