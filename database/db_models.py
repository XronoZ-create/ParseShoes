from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Table
from sqlalchemy.orm import relationship
from database.db import Base, SessionLocal
import random
from datetime import datetime, timedelta


class Shoes(Base):
    __tablename__ = 'shoes'
    id = Column(Integer, primary_key=True)

    platform_id = Column(Integer, ForeignKey("platforms.id"))
    name = Column(String, default="")
    price = Column(String, default="")
    discount_percent = Column(String, default="")
    date = Column(String, default=datetime.now().strftime("%d.%m.%Y %H:%M"))
    img_path = Column(String, default="")

    unique_id = Column(String, default="")

class Platforms(Base):
    __tablename__ = 'platforms'
    id = Column(Integer, primary_key=True)

    name = Column(String)
    shoes = relationship("Shoes", backref="platform")
