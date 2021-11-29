from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class SqlDb(Base):
    engine = create_engine('sqlite:///storage.db', echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    print("Creating Database")

    __tablename__ = 'data'

    location = Column(String, primary_key=True)
    data = Column(String)

    print(f" using {__tablename__} Table ")
