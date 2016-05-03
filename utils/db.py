from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base


engine = create_engine('sqlite:///serial_data.db')
Base.metadata.create_all(engine)
Base.metadata.bind = engine
DBsession = sessionmaker(bind=engine)
session = DBsession()