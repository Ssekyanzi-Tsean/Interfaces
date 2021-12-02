from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String

Base = declarative_base()
engine = create_engine('sqlite:///storage.db', echo=True)


class SqlDb(Base):

    print("Creating Database")

    __tablename__ = 'data'

    location = Column(String, primary_key=True)
    data = Column(String)

    print(f" using {__tablename__} Table ")

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()


if __name__ == "__main__":
    Base.metadata.create_all(engine)
