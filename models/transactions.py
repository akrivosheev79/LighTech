from sqlmodel import SQLModel, Field, Column, JSON
from typing import Optional, List, Literal
import datetime


class Transaction(SQLModel, table=True):

    id: int = Field(default=None, primary_key=True)
    title: str
    #operation: Literal['increase', 'reduce']
    value: int
    created_at: datetime.datetime = Field(
        default_factory=datetime.datetime.utcnow,
    )
    tags: List[str] = Field(sa_column=Column(JSON))

    user_id: Optional[int] = Field(default=None, foreign_key="user.id")

    class Config:
        json_schema_extra = {
            "example": {
                "title": "Transaction example",
                "value": 1000,
                "tags": ["python", "fastapi", "LighTech"]
            }
        }


class Transfer(SQLModel):
    receiver: str
    title: str
    value: int