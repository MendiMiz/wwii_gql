from sqlalchemy.orm import declarative_base

Base = declarative_base()

from .cities import Cities
from .missions import Missions
from .countries import Countries
from .target_types import TargetTypes
from .targets import Targets