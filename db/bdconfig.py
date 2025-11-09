from sqlmodel import SQLModel, create_engine, Session

database = "sqlite:///./db.sqlite"
engine = create_engine(url=database)


def get_session():
    with Session(engine) as session:
        yield session

def create_tables():
    SQLModel.metadata.create_all(engine)