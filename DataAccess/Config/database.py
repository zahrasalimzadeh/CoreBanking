import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

load_dotenv()


def build_connection_string():
    server = os.getenv("DB_SERVER")
    database_name = os.getenv("DB_NAME")
    username = os.getenv("DB_USERNAME")
    password = os.getenv("DB_PASSWORD")
    driver = os.getenv("DB_DRIVER")

    return (
        f"mssql+pyodbc://{username}:{password}@{server}/{database_name}"
        f"?driver={driver}"
        f"&TrustServerCertificate=yes"
    )


connection_string = build_connection_string()
engine = create_engine(connection_string, echo=True)

session_maker = sessionmaker(engine)


@contextmanager
def create_session():
    session = session_maker()
    try:
        yield session
    except Exception as ex:
        session.rollback()
        print(f"Database Exception -> {ex.args[0]}")
        raise
    else:
        session.commit()
    finally:
        session.close()
