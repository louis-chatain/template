from sqlalchemy import Column, Integer, String
from db.database import Base


class DbAbc(Base):
    __tablename__: str = 'abc'
    id: Column[int] = Column(Integer, primary_key=True, index=True, comment='cest quoi un comment sur une collone d`une table')
    username: Column[str] = Column(String(40))