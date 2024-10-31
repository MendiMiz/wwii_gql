from typing import List
from returns.maybe import Maybe
from sqlalchemy import func

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

def update_mission(mission_id, mission_input):
    with session_maker() as session:
        mission_to_update = session.query(Missions).filter(Missions.mission_id == mission_id).first()

        for k, v in mission_input.items():
            setattr(mission_to_update, k, v)

        session.commit()
        session.refresh(mission_to_update)
        return mission_to_update

def create_mission(mission_input):
    with session_maker() as session:
        new_mission_id = session.query(func.max(Missions.mission_id)).scalar() + 1
        mission_to_insert = Missions(
            mission_id=new_mission_id,
            mission_date=mission_input.mission_date,
            airborne_aircraft=mission_input.airborne_aircraft,
            attacking_aircraft=mission_input.attacking_aircraft,
            bombing_aircraft=mission_input.bombing_aircraft,
            aircraft_returned=mission_input.aircraft_returned,
            aircraft_failed=mission_input.aircraft_failed,
            aircraft_damaged=mission_input.aircraft_damaged,
            aircraft_lost=mission_input.aircraft_lost
        )
        session.add(mission_to_insert)
        session.commit()
        session.refresh(mission_to_insert)
        return mission_to_insert
