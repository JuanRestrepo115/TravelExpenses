from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "mssql+pyodbc://@localhost/TravelExpenses?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

base = declarative_base()

def init_db():
    from db.models import UserModel, ExpenseModel

    base.metadata.create_all(bind=engine)
    print("Database tables created successfully.")