from __future__ import annotations
from sqlmodel import SQLModel, Field, Column, JSON, Integer, String
from typing import Optional, List
from pydantic import BaseModel


class User(SQLModel, table=True):

    id: int = Field(default=None, primary_key=True)
    email: str
    password: str
    balance: int = 0
    #transactions: List[Transaction]

    class Config:
        json_schema_extra = {
            "example": {
                "email": "fastapi@lightech.ru",
                "password": "very_strongPa$$w0rd!!"
            }
        }

class TokenResponse(BaseModel):
    access_token: str
    token_type: str

from models.transactions import Transaction
User.update_forward_refs()