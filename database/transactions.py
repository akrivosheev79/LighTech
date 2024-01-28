from sqlmodel import Session, select
from database.connection import engine_url
from models.transactions import Transaction

def add_transaction(transaction: Transaction):
    with Session(engine_url) as session:
        session.add(transaction)
        session.commit()


def get_transactions(id_user: int):
    with Session(engine_url) as session:
        statement = select(Transaction).where(Transaction.user_id == id_user)
        transactions = session.exec(statement).all()

        return transactions
