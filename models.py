from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class SerialData(Base):
    __tablename__ = "serial_data"
    id = Column(Integer, primary_key=True)
    added = Column(DateTime, default=func.now())
    value = Column(String(250))
