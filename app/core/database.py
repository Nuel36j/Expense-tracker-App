"""
SQLAlchemy engine + session setup.
`get_db` is the FastAPI dependency every router/crud function uses
to get a request-scoped DB session.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from app.core.config import settings

connect_args = {}
if settings.DATABASE_URL.startswith("sqlite"):
    # Needed only for SQLite when used with FastAPI's threaded requests
    connect_args = {"check_same_thread": False}

engine = create_engine(settings.DATABASE_URL, connect_args=connect_args)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    """Yield a DB session per-request and always close it afterwards."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
