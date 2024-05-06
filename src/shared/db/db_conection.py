import os.path

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import Session

from shared.base.Base import Base

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "data_base.db")

load_dotenv()

# sqlite_file_name = "database.db"
# url = str(os.getenv('SECRET_BD'))
# url = str(os.getenv('SECRET_BD2'))
DB_USER = str(os.getenv("DB_USER"))
DB_PASS = str(os.getenv("DB_PASS"))
DB_HOST = str(os.getenv("DB_HOST"))
DB_NAME = str(os.getenv("DB_NAME"))
url = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"
url_2 = f"sqlite:///{db_path}"


def get_engine_async():
    return create_async_engine(url_2, echo=True)


def get_engine():
    return create_engine(url_2, echo=True)


def create_db_and_tables():
    Base.metadata.create_all(get_engine())


def get_session():
    # return async_sessionmaker(get_engine_async())
    return Session(get_engine())
