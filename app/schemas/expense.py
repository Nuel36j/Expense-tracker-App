from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field
from typing import Optional

class ExpenseBase(BaseModel):
    amount: float = Field(gt=0)
    category: str
    description: str | None = None
    date: datetime | None = None


class ExpenseCreate(ExpenseBase):
    pass


class ExpenseUpdate(BaseModel):
    amount: Optional[float] | None = Field(default=None, gt=0)
    category: Optional[str] | None = None
    description: Optional[str] | None = None
    date: Optional[datetime] | None = None


class ExpenseOut(ExpenseBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    user_id: int
    created_at: datetime
