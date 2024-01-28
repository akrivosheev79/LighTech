from sqlmodel import Session, select
from database.connection import engine_url
from models.users import User


def add_user(user: User):
    with Session(engine_url) as session:
        session.add(user)
        session.commit()


def get_user(email: str) -> User:
    with Session(engine_url) as session:
        statement = select(User).where(User.email == email)
        users = session.exec(statement).all()

        if len(users) == 0:
            return None

        if len(users) != 1:
            raise ConsistencyException()

        return users[0]

def update_user(user: User):
    with Session(engine_url) as session:
        session.add(user)
        session.commit()
        session.refresh(user)