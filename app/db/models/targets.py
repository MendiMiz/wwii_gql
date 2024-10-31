

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.models import Base


class Targets(Base):
    __tablename__ = "targets"
    target_id = Column(Integer, primary_key=True, autoincrement=True)
    mission_id = Column(Integer, ForeignKey('missions.mission_id'))
    target_industry = Column(String)
    city_id = Column(Integer, ForeignKey('cities.city_id'))
    target_type_id = Column(Integer, ForeignKey('targettypes.target_type_id'))
    target_priority = Column(Integer)

    mission = relationship("Missions", back_populates="target")
    city = relationship("Cities", back_populates="targets")
    target_types = relationship("TargetTypes", back_populates="targets")