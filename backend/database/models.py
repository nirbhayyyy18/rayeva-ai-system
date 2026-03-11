from sqlalchemy import Column, Integer, String
from .database import Base

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    category = Column(String)
    sub_category = Column(String)
    tags = Column(String)

class Proposal(Base):

    __tablename__="proposals"

    id = Column(Integer, primary_key=True)
    budget = Column(Integer)
    event = Column(String)
    audience = Column(String)
    total_cost = Column(Integer)
    impact_summary = Column(String)