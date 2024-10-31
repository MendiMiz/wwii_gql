from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.models import Base


class TargetTypes(Base):
    __tablename__ = "targettypes"
    target_type_id = Column(Integer, primary_key=True, autoincrement=True)
    target_type_name = Column(String, nullable=False)

    targets = relationship("Targets", back_populates="target_types")

