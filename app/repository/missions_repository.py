from typing import List
from returns.maybe import Maybe

from app.db.database import session_maker
from app.db.models import Missions, Targets, Cities, Countries, TargetTypes


def mission_by_id(mission_id: int) -> Maybe[Missions]:
    with session_maker() as session:
        return Maybe.from_optional(session.query(Missions).filter(Missions.mission_id == mission_id).first())

def missions_by_dates_range(start_date, end_date) -> Maybe[List[Missions]]:
    with session_maker() as session:
        return Maybe.from_optional(session.query(Missions)
                                   .filter(Missions.mission_date > start_date, Missions.mission_date < end_date)
                                   .all())

def missions_by_country(country) -> Maybe[List[Missions]]:
    with session_maker() as session:
        return Maybe.from_optional(session.query(Missions)
                                   .join(Targets)
                                   .join(Cities)
                                   .join(Countries)
                                   .filter(Countries.country_name == country)
                                   .all())

def missions_by_target_industry(target_industry: str) -> Maybe[List[Missions]]:
    with session_maker() as session:
        return Maybe.from_optional(session.query(Missions)
                                   .join(Targets)
                                   .filter(Targets.target_industry == target_industry)
                                   .all())

def missions_by_target_type(target_type: str) -> Maybe[List[Missions]]:
    with session_maker() as session:
        return Maybe.from_optional(session.query(Missions)
                                   .join(Targets)
                                   .join(TargetTypes)
                                   .filter(TargetTypes.target_type_name == target_type)
                                   .all())

def delete_mission(mission_id: int):
    with session_maker() as session:
        mission = session.query(Missions).filter(Missions.mission_id == mission_id).first()

        if mission:
            session.delete(mission)
            session.commit()
            return True
        else:
            return False

