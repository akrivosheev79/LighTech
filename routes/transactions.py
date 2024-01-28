from typing import List
from auth.authenticate import authenticate
from fastapi import APIRouter, Body, HTTPException, status, Depends
from models.transactions import Transaction, Transfer
from database.connection import get_session
from database.users import *
from database.transactions import *


transaction_router = APIRouter(
    tags=["Transactions"]
)


@transaction_router.get("/retrieve", response_model=List[Transaction])
async def retrieve_transactions(email: str = Depends(authenticate)) -> dict:

    user = get_user(email)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User does not exist"
        )

    return get_transactions(user.id)


@transaction_router.post("/transfer")
async def create_transaction(transfer: Transfer, email: str = Depends(authenticate)) -> dict:
    user_from = get_user(email)
    user_to = get_user(transfer.receiver)

    if user_from is None or user_to is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User receiver or user sender does not exist. Check it both"
        )

    if user_from.balance - transfer.value < 0:
        raise HTTPException(
            status_code=status.HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS,
            detail=f"User {user_from.email} doesn't have enought money for this operation"
        )

    user_from.balance -= transfer.value
    user_to.balance += transfer.value
    update_user(user_from)
    update_user(user_to)

    transaction_from = Transaction(title=f"Transfer for user {user_to.email}", value=0-transfer.value, user_id=user_from.id)
    transaction_to = Transaction(title=f"Transfer from user {user_from.email}", value=transfer.value, user_id=user_to.id)
    add_transaction(transaction_from)
    add_transaction(transaction_to)

    return {
        "message": "Transfer processed successfully"
    }


@transaction_router.post("/new")
async def create_transaction(transaction: Transaction, email: str = Depends(authenticate)) -> dict:
    user = get_user(email)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User does not exist"
        )

    user.balance += transaction.value
    update_user(user)

    transaction.user_id = user.id
    add_transaction(transaction)

    return {
        "message": "Transaction created successfully"
    }