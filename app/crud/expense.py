from sqlalchemy.orm import Session

from app.models.expense import Expense
from app.schemas.expense import ExpenseCreate, ExpenseUpdate


def get_expense(db: Session, expense_id: int, user_id: int) -> Expense | None:
    return (
        db.query(Expense)
        .filter(Expense.id == expense_id, Expense.user_id == user_id)
        .first()
    )


def get_expenses(
    db: Session, user_id: int, skip: int = 0, limit: int = 100
) -> list[Expense]:
    return (
        db.query(Expense)
        .filter(Expense.user_id == user_id)
        .order_by(Expense.date.desc())
        .offset(skip)
        .limit(limit)
        .all()
    )


def create_expense(db: Session, expense_in: ExpenseCreate, user_id: int) -> Expense:
    db_expense = Expense(**expense_in.model_dump(), user_id=user_id)
    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)
    return db_expense


def update_expense(
    db: Session, db_expense: Expense, expense_in: ExpenseUpdate
) -> Expense:
    for field, value in expense_in.model_dump(exclude_unset=True).items():
        setattr(db_expense, field, value)
    db.add(db_expense)  # explicit add — avoids the "stale session" trap
    db.commit()
    db.refresh(db_expense)
    return db_expense


def delete_expense(db: Session, db_expense: Expense) -> None:
    db.delete(db_expense)
    db.commit()
