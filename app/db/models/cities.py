from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship

from app.db.models import Base


class Cities(Base):
    __tablename__ = "cities"
    city_id = Column(Integer, primary_key=True, autoincrement=True)
    city_name = Column(String, nullable=False)
    country_id = Column(Integer, ForeignKey('countries.country_id'))
    latitude = Column(Float)
    longitude = Column(Float)

    country = relationship("Countries", back_populates="cities")
    targets = relationship("Targets", back_populates="city")
