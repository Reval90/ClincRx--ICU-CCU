from sqlalchemy import create_engine
from models import Base

DATABASE_URL = "sqlite:///clinrx.db"

engine = create_engine(DATABASE_URL)

def create_database():
    Base.metadata.create_all(engine)
    print("ClinRx-ICU-CCU database created successfully")


if __name__ == "__main__":
    create_database()
