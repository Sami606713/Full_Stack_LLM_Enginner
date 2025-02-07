from sqlalchemy import Column,Integer,String
from database.database import Base


class Translation(Base):
    __tablename__="translations"

    id = Column(Integer,primary_key=True,index=True)
    text = Column(String,nullable=False)
    target_language = Column(String,nullable=False)
    translated_text = Column(String,nullable=False)