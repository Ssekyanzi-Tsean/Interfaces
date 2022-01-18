from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String

Base = declarative_base()
engine = create_engine('sqlite:///storage.db', echo=True)


class SqlDb(Base):

    __tablename__ = 'Information'

    location = Column(String, primary_key=True)
    data = Column(String)


if __name__ == "__main__":
    print("Creating Database")
    Base.metadata.create_all(engine)
    #print(f" using {__tablename__} Table ")
