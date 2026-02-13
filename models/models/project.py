from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

from db.base import Base


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    industry_type = Column(String, nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
def __repr__(self):
    return f"<Project(id={self.id}, name='{self.name}')>"
