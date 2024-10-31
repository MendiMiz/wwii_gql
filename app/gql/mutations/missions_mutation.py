from graphene import InputObjectType, Mutation, Field, Date, Float
from sqlalchemy import func

from app.db.database import session_maker
from app.db.models import Missions
from app.gql.types.missions_type import MissionsType


class MissionMutationInput(InputObjectType):
    mission_date = Date()
    airborne_aircraft = Float()
    attacking_aircraft = Float()
    bombing_aircraft = Float()
    aircraft_returned = Float()
    aircraft_failed = Float()
    aircraft_damaged = Float()
    aircraft_lost = Float()




class AddMission(Mutation):
    class Arguments:
        mission_input = MissionMutationInput(required=True)

    mission = Field(MissionsType)

    @staticmethod
    def mutate(root, info, mission_input=None):
        with session_maker() as session:
            new_mission_id = session.query(func.max(Missions.mission_id)).scalar() + 1
            mission_to_insert = Missions(
                mission_id= new_mission_id,
                mission_date=mission_input.mission_date,
                airborne_aircraft =mission_input.airborne_aircraft,
                attacking_aircraft =mission_input.attacking_aircraft,
                bombing_aircraft =mission_input.bombing_aircraft,
                aircraft_returned = mission_input.aircraft_returned,
                aircraft_failed =mission_input.aircraft_failed,
                aircraft_damaged = mission_input.aircraft_damaged,
                aircraft_lost = mission_input.aircraft_lost
            )
            session.add(mission_to_insert)
            session.commit()
            session.refresh(mission_to_insert)
            return AddMission(mission=mission_to_insert)
