from sqlalchemy import create_engine
from .models import Base

DATABASE_URL = "sqlite:///./test.db"  # SQLite database URL

# Create a SQLite engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Create all tables in the database (this creates the tables based on the models)
def init_db():
    Base.metadata.create_all(bind=engine)
